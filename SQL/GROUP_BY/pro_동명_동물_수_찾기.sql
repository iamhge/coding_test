/* 동명 동물 수 찾기 */

-- 코드를 입력하세요
SELECT NAME , COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME != '' -- 이름이 없는 동물은 집계에서 제외
GROUP BY NAME
HAVING COUNT(NAME) >= 2 -- 두 번 이상 쓰인 이름에 대해서
ORDER BY NAME -- 결과는 이름 순서대로