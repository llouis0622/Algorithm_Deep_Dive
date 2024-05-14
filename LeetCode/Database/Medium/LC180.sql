SELECT DISTINCT(L.NUM) AS CONSECUTIVENUMS
FROM (
    SELECT NUM, LAG(NUM) OVER (ORDER BY ID) AS PREV_NUM, LEAD(NUM) OVER (ORDER BY ID) AS POST_NUM
    FROM LOGS
) L
WHERE L.PREV_NUM = L.NUM AND L.NUM = L.POST_NUM;