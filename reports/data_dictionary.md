# Data Dictionary

## 1. fund_master

| Column        | Data Type | Definition                                         |
| ------------- | --------- | -------------------------------------------------- |
| amfi_code     | Integer   | Unique AMFI scheme identifier assigned by AMFI     |
| scheme_name   | String    | Name of the mutual fund scheme                     |
| fund_house    | String    | Asset Management Company (AMC) managing the scheme |
| category      | String    | Broad category of the mutual fund                  |
| sub_category  | String    | Detailed classification within the category        |
| risk_category | String    | Risk level associated with the scheme              |
| launch_date   | Date      | Date on which the scheme was launched              |

---

## 2. nav_history

| Column    | Data Type | Definition                                      |
| --------- | --------- | ----------------------------------------------- |
| amfi_code | Integer   | Unique scheme identifier                        |
| date      | Date      | Date of NAV observation                         |
| nav       | Float     | Net Asset Value of the scheme on the given date |

---

## 3. aum_by_fund_house

| Column     | Data Type | Definition                           |
| ---------- | --------- | ------------------------------------ |
| fund_house | String    | Name of the Asset Management Company |
| date       | Date      | Reporting date                       |
| aum_crore  | Float     | Assets Under Management in crores    |

---

## 4. monthly_sip_inflows

| Column           | Data Type | Definition                                      |
| ---------------- | --------- | ----------------------------------------------- |
| month            | Date      | Reporting month                                 |
| sip_inflow_crore | Float     | Total SIP inflow during the month in crores     |
| yoy_growth_pct   | Float     | Year-over-year growth percentage in SIP inflows |

---

## 5. category_inflows

| Column           | Data Type | Definition                                       |
| ---------------- | --------- | ------------------------------------------------ |
| month            | Date      | Reporting month                                  |
| category         | String    | Mutual fund category                             |
| net_inflow_crore | Float     | Net inflow or outflow for the category in crores |

---

## 6. industry_folio_count

| Column      | Data Type | Definition                                |
| ----------- | --------- | ----------------------------------------- |
| category    | String    | Mutual fund category                      |
| folio_count | Integer   | Number of investor folios in the category |

---

## 7. scheme_performance

| Column             | Data Type | Definition                                 |
| ------------------ | --------- | ------------------------------------------ |
| amfi_code          | Integer   | Unique scheme identifier                   |
| scheme_name        | String    | Name of the mutual fund scheme             |
| fund_house         | String    | Asset Management Company                   |
| category           | String    | Mutual fund category                       |
| plan               | String    | Type of plan (Direct/Regular)              |
| return_1yr_pct     | Float     | One-year annualized return (%)             |
| return_3yr_pct     | Float     | Three-year annualized return (%)           |
| return_5yr_pct     | Float     | Five-year annualized return (%)            |
| benchmark_3yr_pct  | Float     | Benchmark three-year return (%)            |
| alpha              | Float     | Risk-adjusted excess return over benchmark |
| beta               | Float     | Volatility measure relative to benchmark   |
| sharpe_ratio       | Float     | Risk-adjusted return metric                |
| sortino_ratio      | Float     | Downside risk-adjusted return metric       |
| std_dev_ann_pct    | Float     | Annualized standard deviation (%)          |
| max_drawdown_pct   | Float     | Maximum decline from peak value (%)        |
| aum_crore          | Float     | Assets Under Management in crores          |
| expense_ratio_pct  | Float     | Annual fund management expense ratio (%)   |
| morningstar_rating | Integer   | Morningstar rating (1-5)                   |
| risk_grade         | String    | Overall risk grade assigned to the scheme  |

---

## 8. investor_transactions

| Column             | Data Type | Definition                                        |
| ------------------ | --------- | ------------------------------------------------- |
| transaction_id     | Integer   | Unique transaction identifier                     |
| amfi_code          | Integer   | Scheme identifier associated with the transaction |
| transaction_date   | Date      | Date on which the transaction occurred            |
| transaction_type   | String    | Type of transaction (SIP/Lumpsum/Redemption)      |
| transaction_amount | Float     | Value of the transaction                          |
| investor_state     | String    | State of the investor                             |
| kyc_status         | String    | KYC verification status of the investor           |

---

## 9. portfolio_holdings

| Column        | Data Type | Definition                                         |
| ------------- | --------- | -------------------------------------------------- |
| amfi_code     | Integer   | Scheme identifier                                  |
| security_name | String    | Name of the security held                          |
| sector        | String    | Sector to which the security belongs               |
| weight_pct    | Float     | Percentage weight of the security in the portfolio |

---

## 10. benchmark_indices

| Column      | Data Type | Definition                           |
| ----------- | --------- | ------------------------------------ |
| index_name  | String    | Name of the benchmark index          |
| date        | Date      | Date of index observation            |
| index_value | Float     | Closing value of the benchmark index |
