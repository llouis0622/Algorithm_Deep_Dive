SELECT DATE_FORMAT(TRANS_DATE, '%Y-%m') AS MONTH, COUNTRY, COUNT(ID) AS TRANS_COUNT, COUNT(CASE WHEN STATE = 'APPROVED' THEN 1 END) APPROVED_COUNT, SUM(AMOUNT) AS TRANS_TOTAL_AMOUNT,
IFNULL(SUM(CASE WHEN STATE = 'APPROVED' THEN AMOUNT END), 0) AS APPROVED_TOTAL_AMOUNT
FROM TRANSACTIONS
GROUP BY COUNTRY, DATE_FORMAT(TRANS_DATE, '%Y-%M')
ORDER BY MONTH;