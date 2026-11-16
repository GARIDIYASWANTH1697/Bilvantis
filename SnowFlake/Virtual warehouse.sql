-- =====================================================================
-- VIRTUAL WAREHOUSE SCALING EXAMPLES
-- Vertical scaling  = scale UP/DOWN (change WAREHOUSE_SIZE) -> faster complex queries
-- Horizontal scaling = scale OUT/IN (multi-cluster)        -> more concurrent users
-- Note: multi-cluster warehouses require Enterprise Edition or higher.
-- =====================================================================

USE ROLE ACCOUNTADMIN;

-- ---------------------------------------------------------------------
-- 1. VERTICAL SCALING (Scale Up / Scale Down)
-- ---------------------------------------------------------------------

-- Create a small warehouse
CREATE OR REPLACE WAREHOUSE DEMO_VERTICAL_WH
  WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE
  INITIALLY_SUSPENDED = TRUE;

USE WAREHOUSE DEMO_VERTICAL_WH;



-- Run a heavy query on XSMALL (note the elapsed time)
SELECT c_mktsegment, COUNT(*) AS orders, SUM(o_totalprice) AS revenue
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.ORDERS o
JOIN SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.CUSTOMER c ON o.o_custkey = c.c_custkey
GROUP BY c_mktsegment;



-- Disable result cache so the comparison is fair
ALTER SESSION SET USE_CACHED_RESULT = FALSE;


-- Scale UP to LARGE (each size doubles compute & credits/hour)
ALTER WAREHOUSE DEMO_VERTICAL_WH SET WAREHOUSE_SIZE = 'LARGE';


-- Re-run the same query -> should complete faster
SELECT c_mktsegment, COUNT(*) AS orders, SUM(o_totalprice) AS revenue
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.ORDERS o
JOIN SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.CUSTOMER c ON o.o_custkey = c.c_custkey
GROUP BY c_mktsegment;


-- Scale back DOWN to save credits
ALTER WAREHOUSE DEMO_VERTICAL_WH SET WAREHOUSE_SIZE = 'XSMALL';


-- Compare execution times of the two runs
SELECT query_id, warehouse_size, total_elapsed_time/1000 AS seconds, start_time
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY_BY_WAREHOUSE(WAREHOUSE_NAME => 'DEMO_VERTICAL_WH'))
WHERE query_type = 'SELECT'
ORDER BY start_time DESC
LIMIT 5;



-- ---------------------------------------------------------------------
-- 2. HORIZONTAL SCALING (Scale Out / Scale In) - Multi-cluster
-- ---------------------------------------------------------------------

-- Auto-scale mode: MIN < MAX, clusters added when queries queue
CREATE OR REPLACE WAREHOUSE DEMO_HORIZONTAL_WH
  WAREHOUSE_SIZE = 'XSMALL'
  MIN_CLUSTER_COUNT = 1
  MAX_CLUSTER_COUNT = 3
  SCALING_POLICY = 'STANDARD'      -- STANDARD = start clusters quickly; ECONOMY = conserve credits
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE
  INITIALLY_SUSPENDED = TRUE;


-- Switch to ECONOMY policy (only adds a cluster if load lasts ~6 min)
ALTER WAREHOUSE DEMO_HORIZONTAL_WH SET SCALING_POLICY = 'ECONOMY';


-- Maximized mode: MIN = MAX, all clusters always running when warehouse is on
ALTER WAREHOUSE DEMO_HORIZONTAL_WH SET MIN_CLUSTER_COUNT = 3 MAX_CLUSTER_COUNT = 3;


-- Scale back IN to auto-scale between 1 and 2 clusters
ALTER WAREHOUSE DEMO_HORIZONTAL_WH SET MIN_CLUSTER_COUNT = 1 MAX_CLUSTER_COUNT = 2;


-- Limit concurrency per cluster so extra clusters spin up sooner (useful for demos)
ALTER WAREHOUSE DEMO_HORIZONTAL_WH SET MAX_CONCURRENCY_LEVEL = 2;


-- Inspect cluster settings (min/max cluster, running clusters, scaling policy)
SHOW WAREHOUSES LIKE 'DEMO_%';

-- Check whether queries queued (sign you need horizontal scaling)
SELECT start_time, warehouse_name, avg_running, avg_queued_load
FROM TABLE(INFORMATION_SCHEMA.WAREHOUSE_LOAD_HISTORY(
  DATE_RANGE_START => DATEADD('hour', -1, CURRENT_TIMESTAMP()),
  WAREHOUSE_NAME => 'DEMO_HORIZONTAL_WH'));



-- ---------------------------------------------------------------------
-- 3. COMBINED: scale up AND out
-- ---------------------------------------------------------------------
ALTER WAREHOUSE DEMO_HORIZONTAL_WH SET
  WAREHOUSE_SIZE = 'MEDIUM'
  MIN_CLUSTER_COUNT = 1
  MAX_CLUSTER_COUNT = 4
  SCALING_POLICY = 'STANDARD';


-- ---------------------------------------------------------------------
-- 4. CLEANUP
-- ---------------------------------------------------------------------
ALTER SESSION UNSET USE_CACHED_RESULT;
USE WAREHOUSE COMPUTE_WH;
DROP WAREHOUSE IF EXISTS DEMO_VERTICAL_WH;
DROP WAREHOUSE IF EXISTS DEMO_HORIZONTAL_WH;
