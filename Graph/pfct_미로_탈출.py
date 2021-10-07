# 미로 탈출
'''
<입력 예시>
5 6
101010
111111
000001
111111
111111
-> 10
'''
import sys
from collections import deque

input = sys.stdin.readline

def BFS(N: int, M: int, Map: list, root: tuple):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque([root])

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[root[1]][root[0]] = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and Map[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([nx, ny])

                if nx == M-1 and ny == N-1:
                    return visited[ny][nx]
    
    return visited[N-1][M-1]


def main():
    N, M = map(int, input().split())
    Map = [[int(i) for i in list(input().rstrip())] for _ in range(N)]
    
    print(BFS(N, M, Map, (0, 0)))

if __name__=="__main__":
    main()