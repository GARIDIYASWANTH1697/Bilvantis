-- =====================================================================
-- Snowflake TASKS – Concept Examples
-- Uses a demo DB/schema; run top to bottom with ACCOUNTADMIN + COMPUTE_WH
-- =====================================================================

-- 0. Setup ------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS TASKS_DEMO;
CREATE SCHEMA IF NOT EXISTS TASKS_DEMO.DEMO;
USE SCHEMA TASKS_DEMO.DEMO;

CREATE OR REPLACE TABLE raw_orders (order_id INT, amount NUMBER(10,2), region STRING, created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP());
CREATE OR REPLACE TABLE orders_summary (region STRING, total_amount NUMBER(12,2), refreshed_at TIMESTAMP_NTZ);
CREATE OR REPLACE TABLE task_log (task_name STRING, message STRING, logged_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP());

INSERT INTO raw_orders (order_id, amount, region) VALUES
  (1, 100, 'EAST'), (2, 250, 'WEST'), (3, 75, 'EAST'), (4, 300, 'WEST');




-- 1. Interval-scheduled task (every 5 minutes, warehouse) --------------
CREATE OR REPLACE TASK t_heartbeat
  WAREHOUSE = COMPUTE_WH
  SCHEDULE = '5 MINUTE'
AS
  INSERT INTO task_log (task_name, message) VALUES ('T_HEARTBEAT', 'alive');

-- 2. CRON-scheduled task (daily 2 AM UTC) ------------------------------
CREATE OR REPLACE TASK t_daily_summary
  WAREHOUSE = COMPUTE_WH
  SCHEDULE = 'USING CRON 0 2 * * * UTC'
AS
  INSERT OVERWRITE INTO orders_summary
  SELECT region, SUM(amount), CURRENT_TIMESTAMP() FROM raw_orders GROUP BY region;




-- 3. Serverless task (no WAREHOUSE) with size limits -------------------
CREATE OR REPLACE TASK t_serverless_cleanup
  SCHEDULE = '60 MINUTE'
  SERVERLESS_TASK_MAX_STATEMENT_SIZE = 'SMALL'
AS
  DELETE FROM task_log WHERE logged_at < DATEADD('day', -7, CURRENT_TIMESTAMP());




-- 4. Stream-triggered task (runs only when new data arrives) -----------
CREATE OR REPLACE STREAM raw_orders_stream ON TABLE raw_orders;

CREATE OR REPLACE TASK t_process_new_orders
  WAREHOUSE = COMPUTE_WH
  WHEN SYSTEM$STREAM_HAS_DATA('RAW_ORDERS_STREAM')
AS
  INSERT INTO task_log (task_name, message)
  SELECT 'T_PROCESS_NEW_ORDERS', 'new order ' || order_id
  FROM raw_orders_stream WHERE METADATA$ACTION = 'INSERT';




-- 5. Task graph (DAG): root -> 2 children -> finalizer -----------------
--    Includes return values passed parent -> child
CREATE OR REPLACE TASK t_root
  WAREHOUSE = COMPUTE_WH
  SCHEDULE = '60 MINUTE'
AS
BEGIN
  LET cnt NUMBER := (SELECT COUNT(*) FROM raw_orders);
  CALL SYSTEM$SET_RETURN_VALUE(:cnt::VARCHAR);
END;

CREATE OR REPLACE TASK t_child_summary
  WAREHOUSE = COMPUTE_WH
  AFTER t_root
  WHEN SYSTEM$GET_PREDECESSOR_RETURN_VALUE('T_ROOT')::NUMBER > 0
AS
  INSERT OVERWRITE INTO orders_summary
  SELECT region, SUM(amount), CURRENT_TIMESTAMP() FROM raw_orders GROUP BY region;

CREATE OR REPLACE TASK t_child_log
  WAREHOUSE = COMPUTE_WH
  AFTER t_root
AS
BEGIN
  LET cnt VARCHAR := SYSTEM$GET_PREDECESSOR_RETURN_VALUE('T_ROOT');
  INSERT INTO task_log (task_name, message) VALUES ('T_CHILD_LOG', 'row count = ' || :cnt);
END;

CREATE OR REPLACE TASK t_finalizer
  WAREHOUSE = COMPUTE_WH
  FINALIZE = t_root
AS
  INSERT INTO task_log (task_name, message) VALUES ('T_FINALIZER', 'graph run finished');




-- 6. Parameterized task (CONFIG) – run on demand -----------------------
CREATE OR REPLACE TASK t_region_report
  WAREHOUSE = COMPUTE_WH
  CONFIG = $${"region": "EAST"}$$
AS
BEGIN
  LET r STRING := SYSTEM$GET_TASK_GRAPH_CONFIG('region')::STRING;
  INSERT INTO task_log (task_name, message)
  SELECT 'T_REGION_REPORT', :r || ' total = ' || SUM(amount) FROM raw_orders WHERE region = :r;
END;




-- 7. Lifecycle: resume / suspend / run now ----------------------------
-- Tasks are created SUSPENDED. For a graph, resume children first, root last
-- (or enable all at once):
SELECT SYSTEM$TASK_DEPENDENTS_ENABLE('TASKS_DEMO.DEMO.T_ROOT');

ALTER TASK t_process_new_orders RESUME;

-- Run immediately and wait for the whole graph to finish
EXECUTE TASK t_root AWAIT;

-- Run parameterized task with override config
EXECUTE TASK t_region_report USING CONFIG = $${"region": "WEST"}$$ AWAIT;

-


- 8. Modify a task (suspend root first) -------------------------------
ALTER TASK t_root SUSPEND;
ALTER TASK t_root SET SCHEDULE = '30 MINUTE';
ALTER TASK t_root SET SUSPEND_TASK_AFTER_NUM_FAILURES = 3;
ALTER TASK t_root SET USER_TASK_TIMEOUT_MS = 600000;   -- 10 min
ALTER TASK t_child_log MODIFY AS
  INSERT INTO task_log (task_name, message) VALUES ('T_CHILD_LOG', 'modified body');
ALTER TASK t_root RESUME;




-- 9. Monitoring -------------------------------------------------------
SHOW TASKS IN SCHEMA TASKS_DEMO.DEMO;

SELECT name, state, scheduled_time, completed_time, return_value, error_message
FROM TABLE(SNOWFLAKE.INFORMATION_SCHEMA.TASK_HISTORY(
       SCHEDULED_TIME_RANGE_START => DATEADD('hour', -24, CURRENT_TIMESTAMP()),
       SCHEDULED_TIME_RANGE_END   => CURRENT_TIMESTAMP(),
       RESULT_LIMIT => 10000))
WHERE database_name = 'TASKS_DEMO' AND schema_name = 'DEMO'
ORDER BY scheduled_time DESC;

SELECT * FROM task_log ORDER BY logged_at DESC;



-- 10. Cleanup (avoid ongoing credit usage) -----------------------------
ALTER TASK t_root SUSPEND;
ALTER TASK t_process_new_orders SUSPEND;
-- DROP DATABASE TASKS_DEMO;
