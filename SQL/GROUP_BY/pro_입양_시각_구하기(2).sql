/* 입양 시각 구하기(2) */
/*
<참고>
  [Programmers] SQL > GROUP BY > 입양 시각 구하기(2)
   : https://codingspooning.tistory.com/47
*/
-- 1. 변수를 사용하는 방법 (GROUP BY를 사용하지 않음)
-- 코드를 입력하세요
-- ':='은 비교연산자 '='과의 혼동을 피하기 위한 대입 연산
SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) AS HOUR, -- @hour 에 1씩 증가시키며 SELECT문 전체 실행
    (SELECT COUNT(*) 
     FROM ANIMAL_OUTS 
     WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS 
WHERE @hour < 23 -- @hour < 23일 때 까지 계속 증가

-- 2. LEFT JOIN 사용하는 것. BUT 잘 모르겠음..