SELECT P.PRODUCT_NAME, UNIT
FROM PRODUCTS P
INNER JOIN (
    SELECT PRODUCT_ID, SUM(UNIT) AS UNIT
    FROM ORDERS
    WHERE EXTRACT(YEAR_MONTH FROM ORDER_DATE) = '202002'
    GROUP BY PRODUCT_ID
    HAVING SUM(UNIT) >= 100
) O
ON P.PRODUCT_ID = O.PRODUCT_ID;