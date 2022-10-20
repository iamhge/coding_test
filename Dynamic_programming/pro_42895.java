// N으로 표현
/*
<참고 링크>
  Java: ArrayList 2차원 배열 생성
  : https://devyoseph.tistory.com/148
* */
package Dynamic_programming;

import java.util.ArrayList;
import java.util.List;

public class pro_42895 {
    public static int solution(int N, int number) {
        List<Integer>[] dp = new ArrayList[9];
        for (int i = 1; i < 9; i++) {
            dp[i] = new ArrayList<>();
        }

        int nn = N;

        for (int k = 1; k < 9; k ++) {
            dp[k].add(nn);
            nn += Math.pow(10, k)*N;

            for (int n: dp[k]) {
                for (int j = 1; j < 9-k; j ++) {
                    for (int m: dp[j]) {
                        dp[k+j].add(n+m);
                        dp[k+j].add(n*m);
                        if (n > m) {
                            dp[k+j].add(n/m);
                            dp[k+j].add(n-m);
                        }
                        else if (m > n) {
                            dp[k+j].add(m/n);
                            dp[k+j].add(m-n);
                        }
                        else {
                            dp[k+j].add(1);
                        }
                    }
                }
            }
        }

        for (int k = 1; k < 9; k++){
            if (dp[k].contains(number)) {
                return k;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(solution(5, 12));
        System.out.println(solution(5, 31168));
        System.out.println(solution(2, 11));
        System.out.println(solution(1, 1111111));
    }
}
