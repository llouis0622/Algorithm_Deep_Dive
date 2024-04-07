SELECT CUSTOMER_ID, COUNT(VISIT_ID) AS COUNT_NO_TRANS
FROM VISITS
WHERE VISIT_ID NOT IN (
    SELECT VISIT_ID
    FROM TRANSACTIONS
)
GROUP BY CUSTOMER_ID;