SELECT E.BUSINESS_ID
FROM EVENTS E
INNER JOIN (
    SELECT EVENT_TYPE, AVG(OCCURENCES) AVG_OCC
    FROM EVENTS
    GROUP BY EVENT_TYPE
) AVGE
ON E.EVENT_TYPE = AVGE.EVENT_TYPE
WHERE E.OCCURENCES > AVGE.AVG_OCC
GROUP BY E.BUSINESS_ID
HAVING COUNT(E.BUSINESS_ID) >= 2;