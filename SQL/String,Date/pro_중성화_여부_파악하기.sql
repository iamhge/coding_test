/* 중성화 여부 파악하기 */
SELECT ANIMAL_ID, NAME,
    (
        CASE -- 중성화 되어있다면 'O', 아니라면 'X'
            WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
            WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
            ELSE 'X'
        END
    ) AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID -- 아이디 순서