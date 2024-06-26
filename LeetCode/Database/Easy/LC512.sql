SELECT A.PLAYER_ID,
A.DEVICE_ID
FROM ACTIVITY A
INNER JOIN (
	SELECT PLAYER_ID,
	MIN(EVENT_DATE) MIN_DATE
	FROM ACTIVITY
	GROUP BY PLAYER_ID
) AA
ON A.PLAYER_ID = AA.PLAYER_ID
AND A.EVENT_DATE = AA.MIN_DATE;