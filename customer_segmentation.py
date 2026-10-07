import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

RAW_FILE = "customer_data_raw.csv"
OUTPUT_FILE = "customer_segments.csv"

# 1. Load data
df = pd.read_csv(RAW_FILE)

# 2. Remove duplicate records
df = df.drop_duplicates().copy()

# 3. Handle missing numeric values with the median
for col in ["AnnualIncome_k", "SpendingScore"]:
    df[col] = df[col].fillna(df[col].median())

# 4. Select behavioral + demographic features
features = ["Age", "AnnualIncome_k", "SpendingScore", "OrdersPerYear"]

# 5. Scale features before clustering
scaler = StandardScaler()
X = scaler.fit_transform(df[features])

# 6. Elbow method
inertias = []
for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)

plt.plot(range(2, 8), inertias, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# 7. Final K-Means model
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

# 8. Segment labels
summary = df.groupby("Cluster")[features].mean()

names = {}
income_median = summary["AnnualIncome_k"].median()
spend_median = summary["SpendingScore"].median()

for c, row in summary.iterrows():
    if row["AnnualIncome_k"] >= income_median and row["SpendingScore"] >= spend_median:
        names[c] = "High-Value Customers"
    elif row["AnnualIncome_k"] >= income_median:
        names[c] = "High-Income Low-Spend"
    elif row["SpendingScore"] >= spend_median:
        names[c] = "Regular Engaged Customers"
    else:
        names[c] = "Low-Value Customers"

df["Segment"] = df["Cluster"].map(names)

# 9. Save result for GitHub / Power BI
df.to_csv(OUTPUT_FILE, index=False)

# 10. Visualize segments
for segment, group in df.groupby("Segment"):
    plt.scatter(group["AnnualIncome_k"], group["SpendingScore"], s=30, alpha=0.65, label=segment)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.legend()
plt.show()

print("\nCustomer Segment Summary:")
print(df.groupby("Segment")[features].mean().round(2))
print("\nSaved:", OUTPUT_FILE)
