-- =====================================================================
-- TYPES OF STREAMS IN SNOWFLAKE
-- 1. Standard (default)  : tracks INSERT, UPDATE, DELETE
-- 2. Append-only         : tracks INSERT only (standard tables/views)
-- 3. Insert-only         : tracks INSERT only (external / Iceberg tables)
-- Metadata columns: METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID
-- =====================================================================

USE ROLE ACCOUNTADMIN;
USE WAREHOUSE COMPUTE_WH;

CREATE DATABASE IF NOT EXISTS STREAMS_DEMO;
CREATE SCHEMA IF NOT EXISTS STREAMS_DEMO.DEMO;
USE SCHEMA STREAMS_DEMO.DEMO;

-- Source table
CREATE OR REPLACE TABLE STREAMS_DEMO.DEMO.EMPLOYEES (
  id INT, name STRING, salary NUMBER(10,2)
);

INSERT INTO STREAMS_DEMO.DEMO.EMPLOYEES VALUES
  (1, 'Ravi', 50000), (2, 'Anu', 60000), (3, 'Kiran', 55000);

-- ---------------------------------------------------------------------
-- 1. STANDARD STREAM (captures inserts, updates, deletes)
-- ---------------------------------------------------------------------
CREATE OR REPLACE STREAM STREAMS_DEMO.DEMO.EMP_STD_STREAM
  ON TABLE STREAMS_DEMO.DEMO.EMPLOYEES;

-- ---------------------------------------------------------------------
-- 2. APPEND-ONLY STREAM (captures inserts only)
-- ---------------------------------------------------------------------
CREATE OR REPLACE STREAM STREAMS_DEMO.DEMO.EMP_APPEND_STREAM
  ON TABLE STREAMS_DEMO.DEMO.EMPLOYEES
  APPEND_ONLY = TRUE;

-- Make DML changes after streams are created
INSERT INTO STREAMS_DEMO.DEMO.EMPLOYEES VALUES (4, 'Meena', 70000);
UPDATE STREAMS_DEMO.DEMO.EMPLOYEES SET salary = 65000 WHERE id = 2;
DELETE FROM STREAMS_DEMO.DEMO.EMPLOYEES WHERE id = 3;

-- Standard stream: shows INSERT (id 4), UPDATE as DELETE+INSERT pair (id 2,
-- ISUPDATE = TRUE), and DELETE (id 3)
SELECT * FROM STREAMS_DEMO.DEMO.EMP_STD_STREAM;

-- Append-only stream: shows only the new row (id 4)
SELECT * FROM STREAMS_DEMO.DEMO.EMP_APPEND_STREAM;

-- ---------------------------------------------------------------------
-- Consuming a stream (DML that reads it advances the offset)
-- ---------------------------------------------------------------------
CREATE OR REPLACE TABLE STREAMS_DEMO.DEMO.EMPLOYEES_HISTORY (
  id INT, name STRING, salary NUMBER(10,2),
  action STRING, is_update BOOLEAN, captured_at TIMESTAMP_LTZ
);

INSERT INTO STREAMS_DEMO.DEMO.EMPLOYEES_HISTORY
SELECT id, name, salary, METADATA$ACTION, METADATA$ISUPDATE, CURRENT_TIMESTAMP()
FROM STREAMS_DEMO.DEMO.EMP_STD_STREAM;

-- Stream is now empty (offset moved forward)
SELECT * FROM STREAMS_DEMO.DEMO.EMP_STD_STREAM;
SELECT SYSTEM$STREAM_HAS_DATA('STREAMS_DEMO.DEMO.EMP_STD_STREAM');

-- MERGE pattern: apply changes to a target table
CREATE OR REPLACE TABLE STREAMS_DEMO.DEMO.EMPLOYEES_TARGET CLONE STREAMS_DEMO.DEMO.EMPLOYEES;
UPDATE STREAMS_DEMO.DEMO.EMPLOYEES SET salary = 75000 WHERE id = 4;

CREATE OR REPLACE STREAM STREAMS_DEMO.DEMO.EMP_MERGE_STREAM
  ON TABLE STREAMS_DEMO.DEMO.EMPLOYEES SHOW_INITIAL_ROWS = FALSE;
UPDATE STREAMS_DEMO.DEMO.EMPLOYEES SET salary = 80000 WHERE id = 1;

MERGE INTO STREAMS_DEMO.DEMO.EMPLOYEES_TARGET t
USING (SELECT * FROM STREAMS_DEMO.DEMO.EMP_MERGE_STREAM
       WHERE NOT (METADATA$ACTION = 'DELETE' AND METADATA$ISUPDATE)) s
ON t.id = s.id
WHEN MATCHED AND s.METADATA$ACTION = 'DELETE' THEN DELETE
WHEN MATCHED AND s.METADATA$ACTION = 'INSERT' THEN UPDATE SET t.name = s.name, t.salary = s.salary
WHEN NOT MATCHED AND s.METADATA$ACTION = 'INSERT' THEN INSERT (id, name, salary) VALUES (s.id, s.name, s.salary);

SELECT * FROM STREAMS_DEMO.DEMO.EMPLOYEES_TARGET ORDER BY id;

-- ---------------------------------------------------------------------
-- 3. INSERT-ONLY STREAM (external / Iceberg tables only)
-- Requires an existing external table; shown for syntax reference.
-- ---------------------------------------------------------------------
-- CREATE OR REPLACE STREAM STREAMS_DEMO.DEMO.EXT_INSERT_STREAM
--   ON EXTERNAL TABLE STREAMS_DEMO.DEMO.MY_EXTERNAL_TABLE
--   INSERT_ONLY = TRUE;

-- ---------------------------------------------------------------------
-- Stream on a VIEW (requires change tracking on underlying tables)
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW STREAMS_DEMO.DEMO.HIGH_EARNERS AS
SELECT id, name, salary FROM STREAMS_DEMO.DEMO.EMPLOYEES WHERE salary > 60000;

ALTER TABLE STREAMS_DEMO.DEMO.EMPLOYEES SET CHANGE_TRACKING = TRUE;

CREATE OR REPLACE STREAM STREAMS_DEMO.DEMO.HIGH_EARNERS_STREAM
  ON VIEW STREAMS_DEMO.DEMO.HIGH_EARNERS;

INSERT INTO STREAMS_DEMO.DEMO.EMPLOYEES VALUES (5, 'Suresh', 90000);
SELECT * FROM STREAMS_DEMO.DEMO.HIGH_EARNERS_STREAM;

-- ---------------------------------------------------------------------
-- Inspect streams (MODE column shows DEFAULT / APPEND_ONLY / INSERT_ONLY)
-- ---------------------------------------------------------------------
SHOW STREAMS IN SCHEMA STREAMS_DEMO.DEMO;
DESCRIBE STREAM STREAMS_DEMO.DEMO.EMP_STD_STREAM;

-- ---------------------------------------------------------------------
-- Cleanup
-- ---------------------------------------------------------------------
-- DROP DATABASE IF EXISTS STREAMS_DEMO;
