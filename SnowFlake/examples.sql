-- =====================================================================
-- Snowflake SQL Examples (uses SNOWFLAKE_SAMPLE_DATA.TPCH_SF1 — read-only)
-- =====================================================================
USE WAREHOUSE COMPUTE_WH;

-- 1. Basic select with filter and limit
SELECT c_custkey, c_name, c_acctbal, c_mktsegment
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
WHERE c_acctbal > 9000
ORDER BY c_acctbal DESC
LIMIT 10;



-- 2. Aggregation with GROUP BY
SELECT c_mktsegment, COUNT(*) AS customers, ROUND(AVG(c_acctbal), 2) AS avg_balance
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
GROUP BY c_mktsegment
ORDER BY customers DESC;




-- 3. Join + CTE: revenue by nation
WITH order_rev AS (
    SELECT o_custkey, SUM(o_totalprice) AS revenue
    FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS
    GROUP BY o_custkey
)
SELECT n.n_name AS nation, ROUND(SUM(r.revenue), 0) AS total_revenue
FROM order_rev r
JOIN SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER c ON c.c_custkey = r.o_custkey
JOIN SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION   n ON n.n_nationkey = c.c_nationkey
GROUP BY n.n_name
ORDER BY total_revenue DESC
LIMIT 10;



-- 4. Window function + QUALIFY: top 3 customers per segment
SELECT c_mktsegment, c_name, c_acctbal,
       RANK() OVER (PARTITION BY c_mktsegment ORDER BY c_acctbal DESC) AS rnk
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
QUALIFY rnk <= 3;



-- 5. Date functions: monthly order trend
SELECT DATE_TRUNC('month', o_orderdate) AS order_month,
       COUNT(*) AS orders,
       ROUND(SUM(o_totalprice), 0) AS revenue
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS
WHERE o_orderdate >= '1998-01-01'
GROUP BY order_month
ORDER BY order_month;



-- 6. Running total with window frame
SELECT o_orderdate, daily_rev,
       SUM(daily_rev) OVER (ORDER BY o_orderdate ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM (
    SELECT o_orderdate, SUM(o_totalprice) AS daily_rev
    FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS
    WHERE o_orderdate BETWEEN '1998-07-01' AND '1998-07-31'
    GROUP BY o_orderdate
)
ORDER BY o_orderdate;



-- 7. Semi-structured data: parse JSON with VARIANT + FLATTEN
SELECT j.value:name::STRING AS name, j.value:age::INT AS age
FROM (SELECT PARSE_JSON('[{"name":"Ana","age":31},{"name":"Raj","age":27}]') AS data),
     LATERAL FLATTEN(input => data) j;




-- 8. PIVOT: order counts by priority per year
SELECT *
FROM (
    SELECT YEAR(o_orderdate) AS yr, o_orderpriority
    FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS
)
PIVOT (COUNT(o_orderpriority) FOR o_orderpriority IN ANY ORDER BY o_orderpriority)
ORDER BY yr;



-- 9. Generate synthetic data with GENERATOR
SELECT SEQ4() AS id,
       UNIFORM(1, 100, RANDOM()) AS score,
       DATEADD('day', SEQ4(), '2026-01-01')::DATE AS dt
FROM TABLE(GENERATOR(ROWCOUNT => 10));



-- 10. Time Travel / RESULT_SCAN (reuse last query result)
SELECT * FROM TABLE(RESULT_SCAN(LAST_QUERY_ID())) WHERE score > 50;
