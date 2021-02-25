/* 있었는데요 없었습니다 */
-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O
JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID -- O, I 모두 있어야 비교 가능하므로 INNER
WHERE I.DATETIME > O.DATETIME -- 보호시작일보다 입양일이 더 빠른 동물
ORDER BY I.DATETIME -- 보호 시작일이 빠른 순서