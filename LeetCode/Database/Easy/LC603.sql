SELECT SEAT_ID
FROM (
	SELECT SEAT_ID, LAG(FREE) OVER (ORDER BY SEAT_ID) PREV_FREE, FREE, LEAD(FREE) OVER (ORDER BY SEAT_ID) POST_FREE
	FROM SEATS
) S
WHERE (PREV_FREE=1 AND FREE=1) OR (FREE=1 AND POST_FREE=1);