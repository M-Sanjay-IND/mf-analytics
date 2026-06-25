# Mutual Fund Analytics Platform

This project focuses on data ingestion and analysis of the Indian mutual fund ecosystem. The dataset comprises various attributes such as scheme details, historical NAV data, AUM statistics, SIP inflows, investor transactions, portfolio holdings, and benchmark indices.

As part of Day 1, the project involved:

- Loading and validating 10 mutual fund datasets
- Performing data quality and anomaly checks
- Validating AMFI scheme codes across datasets
- Fetching live NAV data using the MFAPI API
- Setting up a structured data analytics workflow

Overall, the quality of the datasets was good, with no duplicate records or other major inconsistencies. Statistical outlier detection methods such as IQR and Z-score were not applied because financial datasets are inherently skewed, and extreme values often represent valid business observations rather than anomalies. Instead, anomaly detection focused on:

- Missing values
- Duplicate records
- Invalid financial values
- Domain-specific validation checks

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLAlchemy
- Requests
- Jupyter Notebook
