#IMPORTS

import pandas as pd
from pathlib import Path as pl

#DIRECTORY WORK

RAW_DIR = pl("data/raw")

print("=" * 80)
print("LOADING DATASETS")
print("=" * 80)

csv_files = sorted(RAW_DIR.glob("*.csv"))

#DATASET TABULATION

if not csv_files:
    print("No CSV files found.")
else:
    for file in csv_files:

        print("\n" + "=" * 80)
        print(f"Dataset: {file.name}")

        try:
            df = pd.read_csv(file)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nHead:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file.name}: {e}")
