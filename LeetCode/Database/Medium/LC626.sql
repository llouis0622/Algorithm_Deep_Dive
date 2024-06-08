SELECT (CASE WHEN MOD(ID, 2) = 0 THEN ID - 1
        WHEN MOD(ID, 2) = 1 AND ID != C.CNT THEN ID + 1
        WHEN MOD(ID, 2) = 1 AND ID = C.CNT THEN ID END) AS ID, STUDENT
FROM SEAT S
INNER JOIN (
    SELECT COUNT(ID) AS CNT
    FROM SEAT
) C
ORDER BY ID;