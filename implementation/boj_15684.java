// 사다리 조작
/*
<풀이 방법>
  - ladder는 H+1개 행, N+1개 열으로 이루어진 배열 (0번째 가로선, 세로선 때문에 1추가)
  - ladder[i][j] = j번째 사다리와 j+1 번째 사다리를 잇는 가로선이 i 위치에 있는가.
  - 백트래킹
<개념 참고 링크>
  [Java] 조합 Combination
  : https://minhamina.tistory.com/38
  점프 투 자바 - 03-07 리스트 (List)
  : https://wikidocs.net/207
* */

package implementation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj_15684 {
    static int n;
    static int h;
    static boolean [][] ladder;

    public static boolean canGoBack(boolean[][] lad) {
        int now; // 현재 위치한 열
        for (int i = 1; i < n+1; i ++) { // 열
            now = i;
            for (int j = 1; j < h+1; j ++) { // 행
                if (lad[j][now]) { // 오른쪽으로 가는 가로선이 있으면
                    now += 1;
                }
                else if (lad[j][now-1]) { // 왼쪽으로 가는 가로선이 있으면
                    now -= 1;
                }
            }
            if (now != i) {
                return false;
            }
        }
        return true;
    }

    public static boolean[][] copyDoubleArr(boolean[][] arr) {
        boolean[][] result = new boolean[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = arr[i].clone();
        }
        return result;
    }

    static boolean dfs (int[] combi, int start, int num) {
        if (num == 0) {
            boolean [][] tmpLadder = copyDoubleArr(ladder);
            for (int c : combi) {
                tmpLadder[c/(n-1)+1][c%(n-1)+1] = true;
            }
            return canGoBack(tmpLadder);
        }
        else {
            for (int i = start; i < (n-1)*h; i++) {
                // 왼쪽이나 오른쪽, 혹은 해당 자리에에 이미 가로선이 있는 경우 -> 9퍼센트에서 계속 시간초과 났었는데 이 코드 추가하고 해결!
                if (ladder[i/(n-1)+1][i%(n-1)] || ladder[i/(n-1)+1][i%(n-1)+2] || ladder[i/(n-1)+1][i%(n-1)+1]) {
                    continue;
                }

                int[] tmpCombi = combi.clone();
                tmpCombi[combi.length - num] = i;
                if (dfs(tmpCombi, i + 1, num - 1)) {
                    return true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // N, M, H
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = input[0];
        h = input[2];
        ladder = new boolean[h+1][n+1];
        int [] line;
        for (int i = 0; i < input[1]; i++) {
            line = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            ladder[line[0]][line[1]] = true;
        }

        // 0
        if (canGoBack(ladder)) {
            System.out.println(0);
            return;
        }
        // combinations
        for (int i = 1; i < Math.min(4, n*h); i++) {
            if (dfs(new int[i], 0, i)) {
                System.out.println(i);
                return;
            }
        }

        System.out.println(-1);
    }
}

// 시간 초과
/*
<풀이 방법>
  - 모든 조합을 구한다.
<오답 노트>
  - 모든 경우의 수를 다 구하고 나서 체크하려니 시간 초과됨.
    경우의 수 구할 때마다 체크하면 시간 단축 가능하다.
*/
/*
package implementation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class boj_15684 {
    static int n;
    static int h;
    static List<List<Integer>> combis = new ArrayList<>();

    public static boolean canGoBack(boolean[][] ladder) {
        int now; // 현재 위치한 열
        for (int i = 1; i < n+1; i ++) { // 열
            now = i;
            for (int j = 1; j < h+1; j ++) { // 행
                if (ladder[j][now]) { // 오른쪽으로 가는 가로선이 있으면
                    now += 1;
                }
                else if (ladder[j][now-1]) { // 왼쪽으로 가는 가로선이 있으면
                    now -= 1;
                }
            }
            if (now != i) {
                return false;
            }
        }
        return true;
    }

    public static boolean[][] copyDoubleArr(boolean[][] arr) {
        boolean[][] result = new boolean[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = arr[i].clone();
        }
        return result;
    }

    static void combination(List<Integer> combi, int start, int num) {
        if (num == 0) {
            combis.add(combi);
        }
        else {
            for (int i = start; i < (n-1)*h; i++) {
                List<Integer> tmpCombi = new ArrayList<>(combi);
                tmpCombi.add(i);
                combination(tmpCombi, i + 1, num - 1);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // N, M, H
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = input[0];
        h = input[2];
        boolean [][] ladder = new boolean[h+1][n+1];
        int [] line;
        for (int i = 0; i < input[1]; i++) {
            line = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            ladder[line[0]][line[1]] = true;
        }

        // 0
        if (canGoBack(ladder)) {
            System.out.println(0);
            return;
        }
        // combinations
        for (int i = 1; i < Math.min(4, n*h); i++) {
            combination(new ArrayList<>(), 0, i);
            boolean [][] tmpLadder;

            for (List<Integer> combi : combis) {
                tmpLadder = copyDoubleArr(ladder);
                for (Integer c : combi) {
                    tmpLadder[c/(n-1)+1][c%(n-1)+1] = true;
                }
                if (canGoBack(tmpLadder)) {
                    System.out.println(i);
                    return;
                }
            }

            combis.clear();
        }

        System.out.println(-1);
    }
}
*/