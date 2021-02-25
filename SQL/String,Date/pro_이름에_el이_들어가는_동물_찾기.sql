/* 이름에 el이 들어가는 동물 찾기 */
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog' -- 이름에 'el'이 들어가는 개
ORDER BY NAME -- 이름 순서