-- Step 1: Set Up Your Workspace & Database

CREATE OR REPLACE DATABASE json_practice_db;

USE DATABASE json_practice_db;

USE SCHEMA public;

-- Make sure you have an active compute warehouse selected
USE WAREHOUSE compute_wh; 




-- Step 3: Create the File Format & Internal Stage

CREATE OR REPLACE FILE FORMAT json_ff
  TYPE = 'JSON'
  STRIP_OUTER_ARRAY = TRUE;


CREATE OR REPLACE STAGE my_internal_stage
  FILE_FORMAT = json_ff;


-- 1. Create the raw landing table
CREATE OR REPLACE TABLE raw_orders (
    raw_data VARIANT
);

-- 2. Copy your staged file into the table
COPY INTO raw_orders
FROM @my_internal_stage/ord.json;

-- 3. Check the loaded rows
SELECT * FROM raw_orders;



-- 1. Parse Flat & Nested Objects (Dot & Colon Notation)
SELECT 
    raw_data:order_id::STRING AS order_id,
    raw_data:order_date::DATE AS order_date,
    raw_data:customer.name::STRING AS customer_name,
    raw_data:customer.city::STRING AS city
FROM raw_orders;



-- 2. Flatten the First Array (items)
SELECT 
    raw_data:order_id::STRING AS order_id,
    raw_data:customer.name::STRING AS customer_name,
    item.value:item_name::STRING AS item_name,
    item.value:price::INT AS price
FROM raw_orders,
LATERAL FLATTEN(INPUT => raw_data:items, OUTER => TRUE) item;




-- 3. Handle Multi-Level Hierarchy (categories inside items)

SELECT 
    raw_data:order_id::STRING AS order_id,
    raw_data:customer.name::STRING AS customer_name,
    item.value:item_name::STRING AS item_name,
    item.value:price::INT AS price,
    cat.value::STRING AS category
FROM raw_orders,
LATERAL FLATTEN(INPUT => raw_data:items, OUTER => TRUE) item,
LATERAL FLATTEN(INPUT => item.value:categories, OUTER => TRUE) cat;



-- 4. Save as a Final Relational Table


CREATE OR REPLACE TABLE clean_order_items AS
SELECT 
    raw_data:order_id::STRING AS order_id,
    raw_data:order_date::DATE AS order_date,
    raw_data:customer.name::STRING AS customer_name,
    raw_data:customer.city::STRING AS city,
    item.value:item_name::STRING AS item_name,
    item.value:price::INT AS price,
    cat.value::STRING AS category
FROM raw_orders,
LATERAL FLATTEN(INPUT => raw_data:items, OUTER => TRUE) item,
LATERAL FLATTEN(INPUT => item.value:categories, OUTER => TRUE) cat;

-- Verify your final relational table!
SELECT * FROM clean_order_items;


SELECT * FROM raw_orders;




-- 1. Simulate a new raw JSON record arriving in raw_orders
INSERT INTO raw_orders (raw_data)
SELECT PARSE_JSON('{
  "order_id": "ORD-103",
  "order_date": "2026-11-21",
  "customer": {"name": "Kiran", "city": "Chennai"},
  "items": [
    {"item_name": "Monitor", "price": 15000, "categories": ["Electronics", "Displays"]}
  ]
}');

-- 2. Incrementally INSERT only the new order into your final table
INSERT INTO clean_order_items (
    order_id, order_date, customer_name, city, item_name, price, category
)
SELECT 
    raw_data:order_id::STRING,
    raw_data:order_date::DATE,
    raw_data:customer.name::STRING,
    raw_data:customer.city::STRING,
    item.value:item_name::STRING,
    item.value:price::INT,
    cat.value::STRING
FROM raw_orders,
LATERAL FLATTEN(INPUT => raw_data:items, OUTER => TRUE) item,
LATERAL FLATTEN(INPUT => item.value:categories, OUTER => TRUE) cat
WHERE raw_data:order_id::STRING = 'ORD-103';

-- 3. Verify your final table now has 6 rows (4 old + 2 new)
SELECT * FROM clean_order_items;

