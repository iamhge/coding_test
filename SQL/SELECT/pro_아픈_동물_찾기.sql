/* 아픈 동물 찾기 */
/*
<개념>
  WHERE 절
   * 행을 선택해서 출력한다.
   * FROM 절 바로 뒤에 위치한다.
   * 연산자 종류 : =, >, >=, <, <=, !=, BETWEEN a AND b, IN list, LIKE, IS NULL, ...
<참고>
  [SQL] 3. 선택해서 출력하자 - WHERE 절
   : https://gomguard.tistory.com/90?category=713994
*/
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'