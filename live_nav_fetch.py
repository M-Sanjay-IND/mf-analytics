import pandas as pd
import requests as req

nav_api = "https://api.mfapi.in/mf/"

mf_schemes = {
        "SBI Bluechip": 119551,
        "ICICI Bluechip": 120503,
        "Nippon Large Cap": 118632,
        "Axis Bluechip": 119092,
        "Kotak Bluechip": 120841
    }

print("=" * 80)

for scheme_name, scheme_code in mf_schemes.items():
    try:
        url = f"{nav_api}{scheme_code}"
        response = req.get(url)
        response.raise_for_status()
        nav_data = response.json()['data']
        nav_df = pd.DataFrame(nav_data)
        nav_df['date'] = pd.to_datetime(nav_df['date'])
        nav_df['nav'] = pd.to_numeric(nav_df['nav'], errors='coerce')
        
        print(f"\n{scheme_name} NAV Data:")
        print(nav_df.head())
        nav_df.to_csv(f"data/raw/{scheme_name.replace(' ', '_')}_nav.csv", index=False)

    except Exception as e:
        print(f"Error fetching data for {scheme_name}: {e}")