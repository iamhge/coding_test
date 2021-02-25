/* 루시와 엘라 찾기 */
/*
<개념>
  IN 연산자
   * 여러 값을 OR 관계로 묶어 나열하는 조건을 WHERE 절에 사용할 때 쓸 수 있는 키워드
   * 하나 이상과 일치하면 조건에 맞는 것으로 평가.
<참고>
  [ANSI SQL] 7. WHERE 절의 조합(AND / OR / NOT / IN)
   : https://inforyou.tistory.com/28
*/
-- OR 연산자 사용
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = 'Lucy' OR NAME = 'Ella' OR NAME = 'Pickle' OR NAME = 'Rogan' OR NAME = 'Sabrina' OR NAME = 'Mitty'

-- IN 연산자 사용
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')