SELECT EVENT_DAY AS DAY, EMP_ID, SUM(OUT_TIME) - SUM(IN_TIME) AS TOTAL_TIME
FROM EMPLOYEES
GROUP BY EVENT_DAY, EMP_ID;
/*
각 직원이 매일 사무실에서 보낸 총 시간을 계산하여 순서에 상관없이 반환
*/