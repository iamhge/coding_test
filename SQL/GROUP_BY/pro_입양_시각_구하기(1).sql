/* 입양 시각 구하기(1) */
/*
<개념>
  날짜 데이터에서 일부 추출
   * YEAR : 연도 추출
   * MONTH : 월 추출
   * DAY : 일 추출 (DAYOFMONTH와 같은 함수)
   * HOUR : 시 추출
   * MINUTE : 분 추출
   * SECOND : 초 추출
<참고>
  [MySQL] 날짜 데이터에서 일부만 추출하기
   : https://extbrain.tistory.com/60
*/
-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20 -- 09:00부터 19:59까지
GROUP BY HOUR(DATETIME) -- 시간대 별
ORDER BY HOUR(DATETIME) -- 시간대 순으로 정렬