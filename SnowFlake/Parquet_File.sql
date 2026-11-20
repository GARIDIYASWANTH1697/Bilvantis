-- 1. Create a Parquet file format
CREATE OR REPLACE FILE FORMAT JSON_PRACTICE_DB.PUBLIC.my_parquet_format
  TYPE = 'PARQUET';



-- 2. Export your clean table as a Parquet file into your stage
COPY INTO @my_internal_stage/orders_export.parquet
FROM JSON_PRACTICE_DB.PUBLIC.clean_order_items
FILE_FORMAT = my_parquet_format
HEADER = TRUE;


-- 3. Verify the .parquet file is now sitting in your stage
LIST @my_internal_stage;


-- Now, query the staged Parquet file directly (notice $1 represents the entire Parquet row as a VARIANT object):


SELECT 
    $1:ORDER_ID::STRING AS order_id,
    $1:CUSTOMER_NAME::STRING AS customer_name,
    $1:ITEM_NAME::STRING AS item_name,
    $1:PRICE::INT AS price
FROM @my_internal_stage/orders_export.parquet
(FILE_FORMAT => 'my_parquet_format');


CREATE OR REPLACE TABLE raw_parquet_orders (
    parquet_data VARIANT
);

COPY INTO raw_parquet_orders
FROM @my_internal_stage/orders_export.parquet
FILE_FORMAT = my_parquet_format;

SELECT * FROM raw_parquet_orders;
