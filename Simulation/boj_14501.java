// 퇴사
/*
<풀이 방법>
  - DFS
  - 해당 날짜에 하거나 안하거나를 기준으로 DFS 했다.
* */
package Simulation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class boj_14501 {
    public static int dfs(int n, int[] root, int[][] schedule) {
        int payment = 0;
        Deque<int[]> stack = new ArrayDeque<>();
        int[] idxPay;
        stack.push(root);
        while (!stack.isEmpty()) {
            idxPay = stack.pop();
            // 모든 날짜를 검사한 경우
            if (idxPay[0] > n-1) {
                if (payment < idxPay[1]) {
                    payment = idxPay[1];
                }
                continue;
            }
            // 기간이 넘쳐서 이번 상담을 못하는 경우
            else if (idxPay[0] + (schedule[idxPay[0]][0] - 1) > n-1) {
                if (payment < idxPay[1]) {
                    payment = idxPay[1];
                }
            }
            // 기간이 넘치지 않는 경우
            else {
                // 이번 상담을 하는 경우
                stack.push(new int[] {idxPay[0] + schedule[idxPay[0]][0], idxPay[1] + schedule[idxPay[0]][1]});
            }
            // 이번 상담을 하지 않고 넘기는 경우
            stack.push(new int[] {idxPay[0] + 1, idxPay[1]});
        }

        return payment;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] schedule = new int[n][2];

        for (int i = 0; i < n; i++) {
            schedule[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        System.out.println(dfs(n, new int[] {0, 0}, schedule));
    }
}

// 다른 사람 풀이
/*
<풀이 방법>
  - Dynamic Programming (DP) (동적 계획법)
  - i번째 날짜 검사시, dp[i]와 dp[i+T[i]]를 함께 갱신한다.
  - dp[i] = i번째 날짜에서 가장 최대의 값.
* */
/*
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(bfr.readLine());
		String[] str = new String[2];
		int[] dp = new int[N+6];
		int[] T = new int[N+6];
		int[] P = new int[N+6];

		for(int i=1;i<=N;i++) {
			str = bfr.readLine().split(" ");
			T[i] = Integer.parseInt(str[0]);
			P[i] = Integer.parseInt(str[1]);
			dp[i] = Math.max(dp[i], dp[i-1]);
			dp[i+T[i]] = Math.max(dp[i+T[i]], dp[i]+P[i]);
		}
        int ans = Math.max(dp[N], dp[N+1]);
		System.out.println(ans);
	}
}
* */