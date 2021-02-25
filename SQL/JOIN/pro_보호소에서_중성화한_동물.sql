/* 보호소에서 중성화한 동물 */
/*
<개념>
  LIKE
   * 문자열의 패턴을 비교한다.
   * '%' : 몇 자리든 비교
   * '_' : 한 자리만 비교
<참고>
  SQL SELECT 기초 #2(Where 조건절, 비교 연산, 문자열 비교, Like Escape)
   : https://sejinworld.tistory.com/18
*/
-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS AS I -- I, O에 모두 기록이 있는 동물이어야 하므로(비교해야하니까), INNER 
JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE 'Intact%' AND O.SEX_UPON_OUTCOME NOT LIKE 'Intact%' -- 보호소에 들어올 때는 중성화되지 않았지만, 보호소를 나갈 때는 중성화된.
ORDER BY I.ANIMAL_ID -- 아이디 순서