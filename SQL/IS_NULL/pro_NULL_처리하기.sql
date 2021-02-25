/* NULL 처리하기 */
/*
<개념>
  CASE 문
   * 형식 ex)
        CASE 컬럼
        WHEN 조건1 THEN 값1
        WHEN 조건2 THEN 값2
        ELSE 값3
        END
   * 형식 ex)
        CASE
        WHEN 컬럼 = 조건1 THEN 값1
        WHEN 컬럼 IS NOT 조건2 THEN 값2
        ELSE 값3
        END
  IFNULL
   * IFNULL(필드, "VALUE")
   * 필드의 값이 NULL을 반환할 때, VALUE로 출력해준다.
   * 하나의 필드 값 뿐 아니라, 연속적으로도 활용할 수 있다.
  COALESCE
   * COALESCE(필드, "VALUE")
   * 필드의 값이 NULL인 경우 VALUE를 반환.
<참고>
  [MSSQL] CASE 문 . 조건에 따라 값 정하기 ! CASE WHEN THEN
   : https://121202.tistory.com/46
  [MySQL] CASE, COALESCE, IFNULL NULL 처리
   : https://syujisu.tistory.com/173
  [SQL] coalesce 함수
   : https://wjjeong.tistory.com/36
*/
-- CASE 문 사용
SELECT ANIMAL_TYPE 
        , (
            CASE
            WHEN NAME IS NULL THEN "No name"
            ELSE NAME
            END
        ) AS NAME
        , SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- IFNULL 사용
SELECT ANIMAL_TYPE 
        , IFNULL(NAME, "No name") as NAME
        , SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- COALESCE 사용
SELECT ANIMAL_TYPE 
        , COALESCE(NAME, "No name") AS NAME
        , SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID