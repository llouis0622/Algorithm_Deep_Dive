SELECT U.NAME, IFNULL(SUM(R.DISTANCE), 0) AS TRAVELLED_DISTANCE
FROM USERS U
LEFT OUTER JOIN RIDES R
ON U.ID = R.USER_ID
GROUP BY U.ID, U.NAME
ORDER BY TRAVELLED_DISTANCE DESC, NAME;