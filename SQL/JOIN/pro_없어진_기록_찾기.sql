/* 없어진 기록 찾기 */
/*
<개념>
  JOIN
   : 두개 이상의 테이블을 결합하여 나타낼 때 이용
  INNER JOIN
   : JOIN하고자 하는 두 테이블에서 공통된 요소들을 통해 결합
   ex)
     SELECT table1.col1, table1.col2, ..., table2.col1, table2.col2, ...
     FROM table1 [table1의 별칭]
     JOIN table2 [table2의 별칭] ON table1.col1 = table2.col2
   * ON뒤에, JOIN시에 두 테이블의 어떤 컬럼을 기준으로 할 지 작성한다.
     위의 예시에서는 table1의 col1 컬럼과 table2의 col2 컬럼이 같은 행들에 대해 JOIN
  OUTER JOIN
   : 두 테이블의 공통영역을 포함해 한쪽 테이블의 다른 데이터를 포함
   * LEFT, RIGHT, FULL JOIN 3개가 있다.
   * LEFT와 OUTER를 정하는 기준 : FROM절에 적어준 테이블이 LEFT,
     JOIN절에 적어준 테이블이 RIGHT.
  CROSS JOIN
   : 특정 기준 없이 두 테이블간 가능한 모든 경우의 수에 대한 결합
   * 특정한 기준이 필요없으므로, ON절이 없음.
  SELF JOIN
   : 자기 스스로를 결합
   * 셀프 조인시에는 별칭을 필수로 입력해주어야 한다.
<참고>
  [MS SQL Server] #12_조인(JOIN)이란 무엇일까?, 기초적인 조인들!
   : https://doorbw.tistory.com/223
  (MySQL) A테이블에 있고, B테이블에 없는 기록 조회
   : https://marlboroyw.tistory.com/292
*/
-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O
LEFT OUTER JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL -- O에는 있으나, I에는 없는 경우
ORDER BY I.ANIMAL_ID