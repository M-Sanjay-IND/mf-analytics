import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

#Directory

processed = Path("data/processed")

print("Processed path:", processed.resolve())
print("Folder exists:", processed.exists())
print("Files found:", list(processed.glob("*.csv")))

#Engine

engine = create_engine("sqlite:///sql/bluestock_mf.db")
with engine.connect() as conn:
    print("Database connection established")

#Database addition

for file in processed.glob("*.csv"):

    print(file.name)

    df = pd.read_csv(file)

    table_name = file.stem

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table_name}",
        engine
    ).iloc[0, 0]

    print(
        f"{table_name}: "
        f"CSV rows = {len(df)}, "
        f"DB rows = {db_rows}"
    )

print("\nAll datasets loaded successfully.")