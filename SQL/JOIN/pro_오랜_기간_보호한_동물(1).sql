/* 오랜 기간 보호한 동물(1) */
-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I
LEFT OUTER JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL -- I에는 있지만, O에는 없는 동물(아직 입양을 못 간 동물)
ORDER BY I.DATETIME -- 보호 시작일 순서
LIMIT 3 -- 가장 오래 보호소에 있었던 동물 3마리