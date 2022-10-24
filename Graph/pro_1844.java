// 게임 맵 최단거리
package Graph;

import java.util.ArrayDeque;
import java.util.Deque;

public class pro_1844 {
    // 상 하 좌 우
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static int bfs(int x, int y, int n, int m, int[][] maps) {
        int[][] visited = new int[n][m];
        Deque<int[]> queue = new ArrayDeque<>();
        int[] xy;
        int i;
        int nx, ny;
        queue.add(new int[] {x, y});
        // 출발지 방문 처리
        visited[x][y] = 1;

        while (!queue.isEmpty()) {
            xy = queue.pop();

            if (xy[0] == n-1 && xy[1] == m-1) {
                return visited[n-1][m-1];
            }

            for (i = 0; i < 4; i ++) {
                nx = xy[0] + dx[i];
                ny = xy[1] + dy[i];
                // 범위가 맞으면
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    // 벽이거나 이미 방문한 노드면 continue
                    if (maps[nx][ny] == 0 || visited[nx][ny] != 0) {
                        continue;
                    }
                    queue.add(new int[] {nx, ny});
                    visited[nx][ny] = visited[xy[0]][xy[1]] + 1;
                }
            }
        }
        return -1;
    }

    public int solution(int[][] maps) {
        int answer = -1;
        int n = maps.length;
        int m = maps[0].length;

        return bfs(0, 0, n, m, maps);
    }
}
