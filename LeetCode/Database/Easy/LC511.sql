SELECT PLAYER_ID,
MIN(EVENT_DATE) FIRST_LOGIN
FROM ACTIVITY
GROUP BY PLAYER_ID;
/*
각 플레이어의 첫 번째 로그인 날짜 반환
*/