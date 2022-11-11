// 야간 전술보행
package implementation;

import java.util.*;

public class pro_133501 {
    public int solution(int distance, int[][] scope, int[][] times) {
        int si, now, start, end;
        int[] security = new int[distance+1]; // security[i] = i 위치에서 근무하는 경비병 index
        
        // security 초기화
        Arrays.fill(security, -1);
        for (si = 0; si < scope.length; si++) {
            start = Math.min(scope[si][0], scope[si][1]);
            end = Math.max(scope[si][0], scope[si][1]);
            
            for (int j = start; j < end+1; j++) {
                security[j] = si;
            }
        }
        
        for (now = 1; now < distance; now++) {
            si = security[now]; // 다음 위치의 경비병 index
            if (si == -1) continue;
            // 경비병의 근무 시간이라면
            if ((now-1) % (times[si][0] + times[si][1]) < times[si][0]) {
                break;
            }
        }
        
        return now;
    }
}