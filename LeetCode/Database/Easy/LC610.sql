SELECT X, Y, Z, CASE
    WHEN X + Y <= Z THEN 'No'
    WHEN Y + Z <= X THEN 'No' 
    WHEN Z + X <= Y THEN 'No' 
    ELSE 'Yes' END AS TRIANGLE
FROM TRIANGLE;
/*
세 개의 선분으로 삼각형을 만들 수 있는지 반환
*/