/* 고양이와 개는 몇 마리 있을까 */
/*
<개념>
  GROUP BY
   * 유형별로 갯수를 알고 싶을 때 사용.
   * 특정 컬럼을 그룹화 -> GROUP BY
   * 특정 컬럼을 그룹화한 결과에 조건을 거는 HAVING
     cf) WHERE : 그룹화 하기 전의 조건
         HAVING : 그룹화 후의 조건 
<참고>
  [MySQL] 그룹화하여 데이터 조회 (GROUP BY)
   : https://extbrain.tistory.com/56
*/
-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Cat' OR ANIMAL_TYPE = 'Dog' -- table에 개, 고양이밖에 없긴 한데 확실하게하기 위해 조건문 삽입
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE -- 고양이를 개보다 먼저 조회