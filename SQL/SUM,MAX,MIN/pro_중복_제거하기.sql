/* 중복 제거하기 */
/*
<개념>
  DISTINCT : 중복 제거(NULL 포함)
  COUNT(DISTINCT) : 중복 제거 + COUNT (NULL 미포함)
<참고>
  [SQL] Null 주의 사항
   : https://tawool.tistory.com/152
*/
-- 코드를 입력하세요
SELECT COUNT(DISTINCT NAME) AS count 
FROM ANIMAL_INS