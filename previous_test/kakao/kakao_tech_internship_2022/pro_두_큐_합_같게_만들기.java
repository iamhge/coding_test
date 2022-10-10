// 두 큐 합 같게 만들기
package previous_test.kakao.kakao_tech_internship_2022;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class pro_118667 {
    public int solution(int[] queue1, int[] queue2) {
        long q1Sum = Arrays.stream(queue1).sum();
        long q2Sum = Arrays.stream(queue2).sum();
        long allSum = q1Sum + q2Sum;

        // 불가능한 경우
        if (allSum % 2 == 1) {
            return -1;
        }

        long allLen = queue1.length + queue2.length;
        Deque<Integer> q1 = new ArrayDeque<>();
        Deque<Integer> q2 = new ArrayDeque<>();

        // deque 초기화
        for (int elem: queue1) {
            q1.add(elem);
        }
        for (int elem: queue2) {
            q2.add(elem);
        }

        int moveNum;
        for (int cnt = 0; cnt < allLen; cnt++) {
            if (q1Sum == q2Sum) {
                return cnt;
            }
            else if (q1Sum > q2Sum) {
                moveNum = q1.pop();
                q2.add(moveNum);
                q1Sum -= moveNum;
                q2Sum += moveNum;
            }
            else {
                moveNum = q2.pop();
                q1.add(moveNum);
                q1Sum += moveNum;
                q2Sum -= moveNum;
            }
        }

        return -1;
    }
}