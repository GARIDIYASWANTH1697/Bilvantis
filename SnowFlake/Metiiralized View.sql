-- =====================================================================
-- Materialized View Examples (requires Snowflake Enterprise Edition+)
-- =====================================================================
USE ROLE ACCOUNTADMIN;
USE WAREHOUSE COMPUTE_WH;

CREATE DATABASE IF NOT EXISTS MV_DEMO;
CREATE SCHEMA IF NOT EXISTS MV_DEMO.SALES;
USE SCHEMA MV_DEMO.SALES;

-- ---------------------------------------------------------------------
-- 0. Sample base table
-- ---------------------------------------------------------------------
CREATE OR REPLACE TABLE MV_DEMO.SALES.ORDERS (
    ORDER_ID     NUMBER,
    CUSTOMER_ID  NUMBER,
    REGION       STRING,
    ORDER_DATE   DATE,
    STATUS       STRING,
    AMOUNT       NUMBER(10,2)
);

INSERT INTO MV_DEMO.SALES.ORDERS
SELECT
    SEQ4()                                              AS ORDER_ID,
    UNIFORM(1, 500, RANDOM())                           AS CUSTOMER_ID,
    ARRAY_CONSTRUCT('EAST','WEST','NORTH','SOUTH')[UNIFORM(0,3,RANDOM())]::STRING AS REGION,
    DATEADD(DAY, -UNIFORM(0, 365, RANDOM()), CURRENT_DATE()) AS ORDER_DATE,
    ARRAY_CONSTRUCT('OPEN','SHIPPED','CANCELLED')[UNIFORM(0,2,RANDOM())]::STRING AS STATUS,
    UNIFORM(10, 1000, RANDOM())::NUMBER(10,2)           AS AMOUNT
FROM TABLE(GENERATOR(ROWCOUNT => 10000));

-- ---------------------------------------------------------------------
-- 1. Simple filtered MV (projection + filter)
-- ---------------------------------------------------------------------
CREATE OR REPLACE MATERIALIZED VIEW MV_DEMO.SALES.MV_SHIPPED_ORDERS AS
SELECT ORDER_ID, CUSTOMER_ID, REGION, ORDER_DATE, AMOUNT
FROM MV_DEMO.SALES.ORDERS
WHERE STATUS = 'SHIPPED';

SELECT * FROM MV_DEMO.SALES.MV_SHIPPED_ORDERS LIMIT 10;

-- ---------------------------------------------------------------------
-- 2. Aggregated MV (daily revenue by region)
-- ---------------------------------------------------------------------
CREATE OR REPLACE MATERIALIZED VIEW MV_DEMO.SALES.MV_DAILY_REGION_REVENUE AS
SELECT
    REGION,
    ORDER_DATE,
    COUNT(*)     AS ORDER_COUNT,
    SUM(AMOUNT)  AS TOTAL_REVENUE,
    MIN(AMOUNT)  AS MIN_ORDER,
    MAX(AMOUNT)  AS MAX_ORDER
FROM MV_DEMO.SALES.ORDERS
GROUP BY REGION, ORDER_DATE;

SELECT * FROM MV_DEMO.SALES.MV_DAILY_REGION_REVENUE
ORDER BY ORDER_DATE DESC, REGION
LIMIT 20;

-- ---------------------------------------------------------------------
-- 3. Clustered MV (different access pattern than base table)
-- ---------------------------------------------------------------------
CREATE OR REPLACE MATERIALIZED VIEW MV_DEMO.SALES.MV_ORDERS_BY_CUSTOMER
    CLUSTER BY (CUSTOMER_ID)
AS
SELECT CUSTOMER_ID, ORDER_ID, ORDER_DATE, STATUS, AMOUNT
FROM MV_DEMO.SALES.ORDERS;

SELECT * FROM MV_DEMO.SALES.MV_ORDERS_BY_CUSTOMER WHERE CUSTOMER_ID = 42;

-- ---------------------------------------------------------------------
-- 4. Secure MV with comment (hides definition from non-owners)
-- ---------------------------------------------------------------------
CREATE OR REPLACE SECURE MATERIALIZED VIEW MV_DEMO.SALES.MV_HIGH_VALUE_ORDERS
    COMMENT = 'Orders above 800 for finance team'
AS
SELECT ORDER_ID, REGION, ORDER_DATE, AMOUNT
FROM MV_DEMO.SALES.ORDERS
WHERE AMOUNT > 800;

-- ---------------------------------------------------------------------
-- 5. Auto-refresh demo: insert into base table, MV updates automatically
-- ---------------------------------------------------------------------
INSERT INTO MV_DEMO.SALES.ORDERS VALUES
    (999999, 1, 'EAST', CURRENT_DATE(), 'SHIPPED', 950.00);

SELECT * FROM MV_DEMO.SALES.MV_SHIPPED_ORDERS WHERE ORDER_ID = 999999;

-- ---------------------------------------------------------------------
-- 6. Management & monitoring
-- ---------------------------------------------------------------------
SHOW MATERIALIZED VIEWS IN SCHEMA MV_DEMO.SALES;

DESCRIBE MATERIALIZED VIEW MV_DEMO.SALES.MV_DAILY_REGION_REVENUE;

ALTER MATERIALIZED VIEW MV_DEMO.SALES.MV_ORDERS_BY_CUSTOMER SUSPEND;
ALTER MATERIALIZED VIEW MV_DEMO.SALES.MV_ORDERS_BY_CUSTOMER RESUME;

-- Refresh cost/history (last 7 days)
SELECT *
FROM TABLE(MV_DEMO.INFORMATION_SCHEMA.MATERIALIZED_VIEW_REFRESH_HISTORY(
    DATE_RANGE_START => DATEADD(DAY, -7, CURRENT_TIMESTAMP())));

-- ---------------------------------------------------------------------
-- Notes / limitations
--  * Single base table only: no joins, UNION, window functions, ORDER BY, LIMIT,
--    HAVING, or non-deterministic functions (e.g. CURRENT_DATE) in the definition.
--  * Background refresh consumes serverless credits.
-- ---------------------------------------------------------------------

-- Cleanup (uncomment to run)
-- DROP DATABASE IF EXISTS MV_DEMO;
