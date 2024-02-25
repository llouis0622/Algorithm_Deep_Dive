SELECT DATE_ID, MAKE_NAME,
COUNT(DISTINCT LEAD_ID) UNIQUE_LEADS,
COUNT(DISTINCT PARTNER_ID) UNIQUE_PARTNERS
FROM DAILYSALES
GROUP BY DATE_ID, MAKE_NAME;
/*
고유한 LEAD_ID와 고유한 PARTNER_ID 개수 반환
*/