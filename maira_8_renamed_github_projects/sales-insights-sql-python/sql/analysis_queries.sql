-- Data Analyst SQL / PL/SQL-style portfolio queries
-- Compatible with Oracle-style SQL concepts. Adapt table names and date functions as needed.

-- 1. Revenue by month and region
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS order_month,
    region,
    ROUND(SUM(quantity * unit_price * (1 - discount_pct)), 2) AS net_revenue,
    COUNT(*) AS orders
FROM sales_orders
WHERE returned = 'No'
GROUP BY TO_CHAR(order_date, 'YYYY-MM'), region
ORDER BY order_month, net_revenue DESC;

-- 2. Product category performance
SELECT
    product_category,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price * (1 - discount_pct)), 2) AS net_revenue,
    ROUND(AVG(discount_pct), 3) AS avg_discount
FROM sales_orders
WHERE returned = 'No'
GROUP BY product_category
ORDER BY net_revenue DESC;

-- 3. Return rate by customer segment
SELECT
    customer_segment,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN returned = 'Yes' THEN 1 ELSE 0 END) AS returned_orders,
    ROUND(SUM(CASE WHEN returned = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS return_rate_pct
FROM sales_orders
GROUP BY customer_segment
ORDER BY return_rate_pct DESC;

-- 4. Example PL/SQL-style procedure for a monthly revenue report
CREATE OR REPLACE PROCEDURE monthly_revenue_report(p_month IN VARCHAR2) AS
BEGIN
    FOR rec IN (
        SELECT region,
               ROUND(SUM(quantity * unit_price * (1 - discount_pct)), 2) AS net_revenue
        FROM sales_orders
        WHERE TO_CHAR(order_date, 'YYYY-MM') = p_month
          AND returned = 'No'
        GROUP BY region
        ORDER BY net_revenue DESC
    ) LOOP
        DBMS_OUTPUT.PUT_LINE(rec.region || ': ' || rec.net_revenue);
    END LOOP;
END;
/
