
SELECT
    fund_house,
    AVG(aum_crore) AS average_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY average_aum DESC
LIMIT 5;


-- 2. Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 3. Monthly SIP YoY Growth

SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflow
ORDER BY month;


-- 4. Number of Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 10 Funds by 5-Year Returns

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Distribution of Funds by Risk Grade

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM scheme_performance
GROUP BY risk_grade
ORDER BY total_funds DESC;


-- 8. Category-wise Net Inflows

SELECT
    category,
    SUM(net_inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;


-- 9. Average Transaction Amount by Transaction Type

SELECT
    transaction_type,
    AVG(transaction_amount) AS average_amount
FROM investor_transactions
GROUP BY transaction_type
ORDER BY average_amount DESC;


-- 10. Maximum NAV Achieved by Each Scheme

SELECT
    amfi_code,
    MAX(nav) AS max_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY max_nav DESC;