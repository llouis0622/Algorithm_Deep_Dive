SELECT P.PROJECT_ID,
ROUND(AVG(E.EXPERIENCE_YEARS), 2) AVERAGE_YEARS
FROM PROJECT P
INNER JOIN
EMPLOYEE E
ON P.EMPLOYEE_ID = E.EMPLOYEE_ID
GROUP BY P.PROJECT_ID;