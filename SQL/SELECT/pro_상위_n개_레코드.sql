/* 상위 n개 레코드 */
/*
<개념>
  1. SELECT MAX(<열>) FROM <테이블 명>, SELECT MIN(<열>) FROM <테이블 명> 
     테이블에서 해당 열의 최댓값 혹은 최솟값을 리턴함.
  2. 1번만 사용하면 최댓값인 열이 나오는 것이 아닌, 그 값만 출력됨.
  3. 따라서 Subquery(서브쿼리)로 작성한다.
<참고>
  (벼락치기) MYSQL (MariaDB) 쿼리 문법 정리
   : https://infinitt.tistory.com/186
  mysql 최대값, 최소값 하나의 row 추출 (MySQL using MAX() with WHERE clauses)
   : https://huskdoll.tistory.com/582
  [MYSQL] Subquery (서브쿼리) 사용법 / select문 안에 select문
   : https://programming119.tistory.com/35
*/
-- 코드를 입력하세요
-- min을 구해서 NAME을 SELECT하는 방법
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS);

-- 상위 1개 row의 NAME을 SELECT하는 방법
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;