SHOW CORTEX BASE MODELS;

--STEP-1) Verify your current role

SELECT CURRENT_ROLE();



-- STEP-2)Check Cortex AI permissions

SHOW GRANTS TO ROLE ACCOUNTADMIN;



-- Step 3 – Enable the required Cortex role

USE ROLE ACCOUNTADMIN;

GRANT DATABASE ROLE SNOWFLAKE.AI_FUNCTIONS_USER
TO ROLE ACCOUNTADMIN;



-- Step 4 – Check available models
SHOW CORTEX BASE MODELS;


-- Step 5 – Execute your first Cortex AI function
SELECT AI_SENTIMENT(
    'The product quality is excellent'
) AS SENTIMENT;



SELECT AI_SENTIMENT(
    'The product quality is excellent',
    [],
    TRUE
) AS RESULT;


SELECT AI_COMPLETE(
    'llama3.3-70b',
    'Explain Snowflake in simple English'
);



-- Step 6 – Sample reviews dataset (inline, no table needed)
WITH reviews AS (
    SELECT * FROM VALUES
        (1, 'The product quality is excellent, delivery was fast!'),
        (2, 'Terrible support, I waited 3 weeks for a refund.'),
        (3, 'Decent value for the price, but packaging was damaged.'),
        (4, 'Absolutely love it, will buy again.')
    AS t(review_id, review_text)
)
SELECT
    review_id,
    review_text,
    AI_SENTIMENT(review_text)                                         AS sentiment,
    AI_CLASSIFY(review_text, ['Quality', 'Delivery', 'Support', 'Price']):labels[0]::STRING AS category,
    AI_TRANSLATE(review_text, 'en', 'fr')                             AS review_fr,
    AI_FILTER(PROMPT('Is this customer complaining? {0}', review_text)) AS is_complaint
FROM reviews;

-- Step 7 – Summarize many rows into one answer
SELECT AI_SUMMARIZE_AGG(review_text) AS overall_summary
FROM VALUES
    ('Fast shipping and great quality.'),
    ('Support was slow to respond.'),
    ('Good price, average build quality.') AS t(review_text);

-- Step 8 – Extract structured fields from free text
SELECT AI_EXTRACT(
    text => 'Order #4521 from John Smith, shipped to Austin TX on 2026-10-02.',
    responseFormat => {'order_id': 'What is the order number?',
                       'customer': 'Who is the customer?',
                       'city': 'Which city was it shipped to?'}
) AS extracted;

-- Step 9 – Semantic similarity between two texts (0–1)
SELECT AI_SIMILARITY('How do I reset my password?',
                     'I forgot my login credentials') AS similarity;

-- Step 10 – AI_COMPLETE with a system prompt and options
SELECT AI_COMPLETE(
    model => 'llama3.3-70b',
    prompt => 'Write a 2-line tagline for a coffee shop.',
    model_parameters => {'temperature': 0.7, 'max_tokens': 100}
) AS tagline;

-- Step 11 – Estimate token count before running a prompt
SELECT AI_COUNT_TOKENS('ai_complete', 'llama3.3-70b',
                       'Explain Snowflake in simple English') AS tokens;