/* 모든 레코드 조회하기 */
/*
<개념>
  ORDER BY 절
   * 결과물을 오름차 순, 혹은 내림차 순으로 정렬하여 출력한다.
   * 항상 SELECT 문의 맨 마지막에 위치한다.
   * ASC : 오름차 순, DESC : 내림차 순
<참고>
  [SQL] 4. 정렬해서 출력하기 - ORDER BY 절
   : https://gomguard.tistory.com/93
*/
-- 코드를 입력하세요
SELECT * 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC