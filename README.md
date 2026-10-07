# Customer Segmentation Project

## Thiranex – Data Analytics Task 2

### Objective
Segment customers based on demographic and behavioral characteristics, analyze purchase patterns, visualize customer groups, and generate targeted business insights.

## Workflow
1. Load customer data
2. Remove duplicate records
3. Handle missing values
4. Explore customer attributes
5. Standardize clustering features
6. Use the Elbow Method to inspect the suitable number of clusters
7. Apply K-Means clustering
8. Label customer segments
9. Visualize segment characteristics
10. Export the segmented dataset for further analysis / Power BI

## Features Used
- Age
- Annual Income
- Spending Score
- Orders Per Year

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- K-Means Clustering
- Jupyter Notebook
- Power BI-ready CSV output

## Segment Interpretation
The project maps clusters into business-friendly groups:
- High-Value Customers
- High-Income Low-Spend
- Regular Engaged Customers
- Low-Value Customers

## Files
- `customer_data_raw.csv` – sample input data with a few missing/duplicate records for preprocessing
- `customer_segments.csv` – cleaned data with cluster and segment labels
- `customer_segmentation.py` – complete Python implementation
- `customer_segmentation.ipynb` – notebook version
- `outputs/` – generated charts and cluster summary

## Note
The included dataset is a self-contained sample customer dataset created for demonstrating the segmentation workflow. The project can also be adapted to a Thiranex-provided dataset if the tutorial specifies a different input file.
