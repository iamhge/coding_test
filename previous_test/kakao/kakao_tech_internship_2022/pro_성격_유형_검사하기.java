/*
<개념 참고 링크>
  [class] Java - HashMap (해시맵) - key=value 쌍의 유사 배열. (Python Dictionary와 유사)
  : https://homzzang.com/b/java-42
  자바에서 파이썬의 defaultdict 처럼 초기값을 가지는 Map 사용하기
  : https://velog.io/@sojukang/%EC%9E%90%EB%B0%94%EC%97%90%EC%84%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-DefaultDict-%EC%B2%98%EB%9F%BC-%EC%B4%88%EA%B8%B0%EA%B0%92%EC%9D%84-%EA%B0%80%EC%A7%80%EB%8A%94-Map-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
  Java - HashMap에서 key로 value 업데이트
  : https://codechacha.com/ko/java-how-to-update-value-of-key-from-hashmap/
  자바 String 문자열 사용법 정리
  : https://yeolco.tistory.com/30
  [String에서 한 글자씩 읽기/추출하는 방법]
  : https://4369.tistory.com/entry/String%EC%97%90%EC%84%9C-%ED%95%9C-%EA%B8%80%EC%9E%90%EC%94%A9-%EC%9D%BD%EA%B8%B0%EC%B6%94%EC%B6%9C%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
  [Java] 배열의 여러가지 선언 및 초기화 방법
  : https://coding-factory.tistory.com/253
*/
package previous_test.kakao.kakao_tech_internship_2022;

import java.util.HashMap;
import java.util.Map;

class pro_118666 {
    public static Map<Character, Integer> elem = new HashMap<>();
    public static int n;
    public static char[] type = {'R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'};
    
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        n = survey.length;
        
        for (int i = 0 ; i < n; i ++) {
            if (choices[i] <= 3){
                elem.put(survey[i].charAt(0), elem.getOrDefault(survey[i].charAt(0), 0) + 4 - choices[i]);
            }
            else {
                elem.put(survey[i].charAt(1), elem.getOrDefault(survey[i].charAt(1), 0) + choices[i] - 4);
            }
        }
        for (int i = 0; i < 8; i += 2){
            if (elem.getOrDefault(type[i], 0) >= elem.getOrDefault(type[i+1], 0)) {
                answer += type[i];
            }
            else {
                answer += type[i+1];
            }
        }
        
        return answer;
    }
}