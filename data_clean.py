import pandas as pd
from pathlib import Path as pl

#Directory

raw = pl('./data/raw')
processed = pl('./data/processed')

#Cleaning nav_history.csv

his_df = pd.read_csv(raw / '02_nav_history.csv')

his_df['date'] = pd.to_datetime(his_df['date'], format='%Y-%m-%d')

his_df = his_df.sort_values(by=['amfi_code', 'date'], ascending=True)

if (his_df.isnull().sum().sum() > 0):
    his_df['nav'] = (his_df.groupby('amfi_code')['nav'].ffill())

his_df.drop_duplicates(subset=['amfi_code', 'date'], keep='last', inplace=True)

his_df.drop(his_df.query('nav <= 0').index, inplace=True)

if his_df is not None and not his_df.empty:
    his_df.to_csv(processed / 'processed_nav_history.csv', index=False)
    print("\nProcessed nav_history.csv saved successfully.")



#Cleaning investor_transactions.csv

trans_df = pd.read_csv(raw / '08_investor_transactions.csv')

trans_df['transaction_date'] = pd.to_datetime(trans_df['transaction_date'], format='%Y-%m-%d')

standard_types = {
    "SIP": "SIP",
    "Redemption": "REDEMPTION",
    "Lumpsum": "LUMPSUM",
}

trans_df['transaction_type'] = trans_df['transaction_type'].map(standard_types)

trans_df = trans_df[trans_df['amount_inr'] > 0]

valid_kyc = [
    'Verified',
    'Pending',
    'Rejected'
]

invalid = trans_df[~trans_df["kyc_status"].isin(valid_kyc)]

if len(invalid) > 0:
    print("\nInvalid KYC values found:")
    print(invalid['kyc_status'].unique())
else:
    print("\nAll KYC status values are valid.")

if trans_df is not None and not trans_df.empty:
    trans_df.to_csv(processed / 'processed_investor_transactions.csv', index=False)
    print("\nProcessed investor_transactions.csv saved successfully.")

#Cleaning scheme_performance.csv

perf_df = pd.read_csv(raw / '07_scheme_performance.csv')

return_cols = [
    col for col in perf_df.columns if "return" in col.lower()
]

for col in return_cols:
    perf_df[col] = pd.to_numeric(perf_df[col], errors="coerce")

anomalies = perf_df[(perf_df["expense_ratio_pct"] < 0.1) | (perf_df["expense_ratio_pct"] > 2.5)]

print(f"Number of anomalies found: {len(anomalies)}")

if perf_df is not None and not perf_df.empty:
    perf_df.to_csv(processed / 'processed_scheme_performance.csv', index=False)
    print("\nProcessed scheme_performance.csv saved successfully.")

#Cleaning other files

def clean(file_path, processed_dir, output_name=None):

    df = pd.read_csv(file_path)

    df.drop_duplicates(inplace=True)

    for col in df.columns:
        if 'date' in col.lower() or 'month' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')

    sort_cols = []

    if 'amfi_code' in df.columns:
        sort_cols.append('amfi_code')

    for col in df.columns:
        if 'date' in col.lower() or 'month' in col.lower():
            sort_cols.append(col)

    if sort_cols:
        df = df.sort_values(by=sort_cols)

    for col in df.columns:
        if col != 'yoy_growth_pct':
            df[col] = df[col].ffill()

    if output_name is None:
        output_name = file_path.name

    output_path = processed_dir / output_name

    df.to_csv(output_path, index=False)

    print(f"{output_name} cleaned and saved.")

    return df

#Files to clean using clean function

clean_files = ['01_fund_master.csv', '03_aum_by_fund_house.csv', '04_monthly_sip_inflows.csv', '05_category_inflows.csv', '06_industry_folio_count.csv', '09_portfolio_holdings.csv', '10_benchmark_indices.csv',]

for file_name in clean_files:
    file_path = raw / file_name
    new_file_name = f"processed_{file_name.strip('.csv')[3:]}.csv"
    clean(file_path, processed, new_file_name)