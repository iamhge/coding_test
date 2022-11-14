// 롤케이크 자르기
/*
<풀이 방법>
  - 왼쪽(young), 오른쪽(old)에서부터 토핑 종류의 누적합을 구한다.
  - young[i] == old[i+1]이 될 때 answer++
* */
package implementation;

import java.util.*;

public class pro_132265 {
    public int solution(int[] topping) {
        int answer = 0;
        int i, j;

        HashSet<Integer> youngSet = new HashSet<>(); // 왼쪽에서부터 토핑 종류를 저장
        HashSet<Integer> oldSet = new HashSet<>(); // 오른쪽에서부터 토핑 종류를 저장

        int[] young = new int[topping.length]; // 왼쪽 끝에서부터 토핑 종류의 개수 누적합
        int[] old = new int[topping.length]; // 오른쪽 끝에서부터 토핑 종류의 개수 누적합

        // 맨끝의 수 초기화
        youngSet.add(topping[0]);
        oldSet.add(topping[topping.length-1]);
        young[0] = 1;
        old[topping.length-1] = 1;

        for (i = 1; i < topping.length; i++) {
            if (!youngSet.contains(topping[i])) {
                young[i]++;
                youngSet.add(topping[i]);
            }
            young[i] += young[i-1];

            j = topping.length-1 - i;
            if (!oldSet.contains(topping[j])) {
                old[j]++;
                oldSet.add(topping[j]);
            }
            old[j] += old[j+1];
        }

        for (i = 0; i < topping.length-1; i++) {
            if (young[i] == old[i+1]) {
                answer++;
            }
            else if (young[i] > old[i+1]) {
                break;
            }
        }

        return answer;
    }
}

// 다른 사람 코드
/*
<풀이 방법>
  - map을 이용한 풀이.
  1) 각 토핑의 개수를 toppingCnt[토핑]에 저장한다.
  2) topping 배열을 순회하며 토핑을 하나씩 뽑고, toppingCnt[나온 토핑]의 개수를 줄인다.
     이 때, toppingCnt[나온 토핑]이 0이 되면 해당 키를 삭제한다.
  3) 뽑은 토핑의 개수를 cnt 라고 할 때, cnt와 toppingCnt.size()가 같아지면 answer++
* */
/*
import java.util.HashMap;
import java.util.Map;

class Solution {

    public int solution(int[] topping) {

        int answer = 0;

        Map<Integer, Integer> map1 = new HashMap<>();
        Map<Integer, Integer> map2 = new HashMap<>();

        for (int i = 0; i < topping.length; i++) {
            map2.put(topping[i], map2.getOrDefault(topping[i], 0) + 1);
        }

        for (int i = 0; i < topping.length - 1; i++) {

            map1.put(topping[i], map1.getOrDefault(topping[i], 0) + 1);

            int cnt = map2.getOrDefault(topping[i], 0);
            if (cnt > 1) {
                map2.put(topping[i], cnt - 1);
            } else {
                map2.remove(topping[i]);
            }

            if (map1.keySet().size() == map2.keySet().size()) {
                answer += 1;
            }
        }

        return answer;
    }
}
* */

// 시간 초과
/*
public class pro_132265 {
    public int solution(int[] topping) {
        int answer = 0;

        HashSet<Integer> young = new HashSet<>();
        HashSet<Integer> old;
        for (int i = 0; i < topping.length; i++) {
            young.add(topping[i]);
            old = Arrays.stream(Arrays.copyOfRange(topping, i, topping.length)).boxed().collect(Collectors.toCollection(HashSet::new));
            if (old.size() == young.size()) {
                answer++;
            }
            else if (old.size() < young.size()) {
                break;
            }
        }

        return answer;
    }
}
 */