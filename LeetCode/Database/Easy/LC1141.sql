SELECT ACTIVITY_DATE AS DAY,
COUNT(DISTINCT USER_ID) AS ACTIVE_USERS
FROM ACTIVITY
WHERE DATE_SUB('2019-07-27', INTERVAL 30 DAY) < ACTIVITY_DATE
AND ACTIVITY_DATE <= '2019-07-27'
GROUP BY ACTIVITY_DATE;