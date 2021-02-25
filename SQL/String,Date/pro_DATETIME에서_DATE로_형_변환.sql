/* DATETIME에서 DATE로 형 변환 */
/*
<개념>
  문자열 자르기
   * LEFT(문자열, 길이) : 왼쪽에서부터 문자열을 원하는 길이만큼 잘라 리턴
   * RIGHT(문자열, 길이) : 오른쪽에서부터 문자열을 원하는 길이만큼 잘라 리턴
   * SUBSTRING(문자열, 시작 자리 번호, 자를 문자 수) : 지정한 위치에서부터 원하는 길이만큼 문자열을 잘라 리턴
<참고>
  [MSSQL] 문자열 자르기 (LEFT,RIGHT,SUBSTRING) 사용법 & 예제
   : https://coding-factory.tistory.com/99
*/
SELECT ANIMAL_ID, NAME, LEFT(DATE(DATETIME), 10) AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID