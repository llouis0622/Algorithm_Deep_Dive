SELECT P.PRODUCT_ID, IFNULL(PP.NEW_PRICE, 10) PRICE
FROM  (
    SELECT DISTINCT PRODUCT_ID
    FROM PRODUCTS
) P
LEFT OUTER JOIN (
    SELECT PRODUCT_ID, NEW_PRICE
    FROM (
        SELECT PRODUCT_ID, NEW_PRICE, RANK() OVER (PARTITION BY PRODUCT_ID ORDER BY CHANGE_DATE DESC) RK_DATE
        FROM PRODUCTS
        WHERE CHANGE_DATE <= '2019-08-16'
    ) A
    WHERE RK_DATE = 1
) PP
ON P.PRODUCT_ID = PP.PRODUCT_ID;