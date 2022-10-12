// 아기 상어
/*
<풀이 방법>
  - bfs + recursion
  - 그 때 그 때 가장 가까운 물고기를 찾아 먹은 후,
    물고기를 먹고 나면 새로이 bfs 탐색을 시작한다.
* */
package Simulation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class boj_16236 {
    // 상 좌 우 하
    public static int[] dx = {-1, 0, 0, 1};
    public static int[] dy = {0, -1, 1, 0};

    public static int bfs(int n, int[] root, int[][] map, int babySize, int eat) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(root);
        int[] now = new int[3];
        int nx, ny, x, y, time;
        boolean[][] visited = new boolean[n][n];
        int closestTime = root[2] + n*n + 1;
        int closestX = n;
        int closestY = n;

        while (!queue.isEmpty()) {
            now = queue.pop();
            x = now[0];
            y = now[1];
            time = now[2];


            if (closestTime < time) {
                continue;
            }

            if (map[x][y] < babySize && map[x][y] != 0) {
                closestTime = time;
                if (closestX > x) {
                    closestX = x;
                    closestY = y;
                }
                else if (closestX == x && closestY > y) {
                    closestY = y;
                }
            }
            else {
                for (int i = 0; i < 4; i++) {
                    nx = x + dx[i];
                    ny = y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < n){
                        if (visited[nx][ny] || map[nx][ny] > babySize) continue;
                        queue.add(new int[] {nx, ny, time+1});
                        visited[nx][ny] = true;
                    }
                }
            }

        }

        // 더 이상 먹을 수 있는 물고기가 없는 경우
        if (closestTime == root[2] + n*n + 1) {
            return root[2];
        }

        map[closestX][closestY] = 0;
        eat += 1;
        if (babySize == eat) {
            babySize += 1;
            eat = 0;
        }
        return bfs(n, new int[] {closestX, closestY, closestTime}, map, babySize, eat);
    }


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        int[] root = new int[3];

        for (int i = 0; i < n; i++) {
            map[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 9) {
                    root = new int[] {i, j, 0};
                    map[i][j] = 0;
                }

            }
        }
        System.out.println(bfs(n, root, map, 2, 0));
    }
}

// 틀린 풀이
/*
<풀이 방법>
  - bfs + recursion
  - 그 때 그 때 가장 가까운 물고기를 찾아 먹은 후,
    물고기를 먹고 나면 새로이 bfs 탐색을 시작한다.
<오답 노트>
  - 상 좌 우 하 순으로 탐색하면 가장 가까운 물고기 중 최상단 좌측의 물고기를 선택할 줄 알았는데, 그렇지 않다.
반례)
예제 입력 4의 경우,
x = 0, y = 2, time = 10, babySize = 4인 상태의 맵은 다음과 같다.
[5, 4, 0, 0, 3, 4]
[4, 3, 0, 3, 4, 5]
[3, 2, 0, 5, 6, 6]
[2, 0, 0, 3, 4, 5]
[3, 2, 0, 6, 5, 4]
[6, 6, 6, 6, 6, 6]
이 떼, 다음으로 (0, 4)의 물고기를 먹어야하는데,
기존 방법으로 탐색하면 (1, 1)의 물고기를 먹는다.
* */
/*
package Simulation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class boj_16236 {
    // 상 좌 우 하
    public static int[] dx = {-1, 0, 0, 1};
    public static int[] dy = {0, -1, 1, 0};

    public static int bfs(int n, int[] root, int[][] map, int babySize, int eat) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(root);
        int[] now = new int[3];
        int nx, ny, x, y, time;
        boolean[][] visited = new boolean[n][n];

        while (!queue.isEmpty()) {
            now = queue.pop();
            x = now[0];
            y = now[1];
            time = now[2];
            visited[x][y] = true;

            if (map[x][y] < babySize && map[x][y] != 0) {
                map[x][y] = 0;
                eat += 1;
                System.out.println("x = "+ x + ", y = " + y + ", time = " + time + ", babySize = " + babySize);
                for (int[] m: map) {
                    System.out.println(Arrays.toString(m));
                }
                if (babySize == eat) {
                    babySize += 1;
                    eat = 0;
                }

                return bfs(n, new int[] {x, y, time}, map, babySize, eat);
            }

            for (int i = 0; i < 4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n){
                    if (visited[nx][ny] || map[nx][ny] > babySize) continue;
                    queue.add(new int[] {nx, ny, time+1});
                }
            }
        }
        return root[2];
    }


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        int[] root = new int[3];

        for (int i = 0; i < n; i++) {
            map[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 9) {
                    root = new int[] {i, j, 0};
                    map[i][j] = 0;
                }

            }
        }
        System.out.println(bfs(n, root, map, 2, 0));
    }
}
*/