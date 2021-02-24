/* 어린 동물 찾기*/
/*
어린 -> not 'Aged'
*/
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'