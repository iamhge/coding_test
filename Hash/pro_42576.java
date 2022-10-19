// 완주하지 못한 선수
package Hash;

import java.util.Arrays;

public class pro_42576 {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i = 0; i < completion.length; i ++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }

        return participant[participant.length-1];
    }
}
// HashMap으로 다시 풀이
/*
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> pc = new HashMap<>();

        for (String p: participant) {
            pc.put(p, pc.getOrDefault(p, 0) + 1);
        }
        for (String c: completion) {
            pc.put(c, pc.get(c) - 1);
        }
        for (Map.Entry<String, Integer> entry: pc.entrySet()) {
            if (entry.getValue() > 0) {
                return entry.getKey();
            }
        }

        return "";
    }
}
* */

// 다른 사람 풀이
// HashMap 을 이용한 풀이
/*
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion) hm.put(player, hm.get(player) - 1);

        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
}
*/