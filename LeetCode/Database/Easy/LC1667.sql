SELECT USER_ID, CONCAT(UPPER(SUBSTR(NAME, 1, 1)), LOWER(SUBSTR(NAME, 2))) NAME
FROM USERS
ORDER BY USER_ID;