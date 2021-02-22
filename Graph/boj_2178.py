# 미로 탐색
'''
<아이디어>
  BFS를 이용해 미로를 탐색한다.
  visited[x][y]에 출발지에서부터 (x, y)좌표까지 가는 데에 걸린 칸수를 적는다.
<해경이의 뇌피셜 Q&A>
  Q. 최적이 아닌 경로가 먼저 골인하면 어떡하지?
  A. BFS는 너비 우선 탐색이므로, 경로의 길이가 균일하게 퍼진다.
     따라서 최적이 아닌 경로가 먼저 골인하지 않는다.
<참고>
  [파이썬] 백준 2178번 미로 탐색 - BFS 최단 경로 탐색
   : https://chancoding.tistory.com/64
'''
import sys
from collections import deque

def mazeOpt(N: int, M: int, Map: list, root: tuple):
    visited = [[0]*M for _ in range(N)]
    queue = deque([root])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if (x, y) == (N-1, M-1):
            break
        if x != 0 and Map[x-1][y] and visited[x-1][y] == 0: # 상
            visited[x-1][y] = visited[x][y] + 1
            queue.append((x-1, y))
        if x != N-1 and Map[x+1][y] and visited[x+1][y] == 0: # 하
            visited[x+1][y] = visited[x][y] + 1
            queue.append((x+1, y))
        if y != 0 and Map[x][y-1] and visited[x][y-1] == 0: # 좌
            visited[x][y-1] = visited[x][y] + 1
            queue.append((x, y-1))
        if y != M-1 and Map[x][y+1] and visited[x][y+1] == 0: # 우
            visited[x][y+1] = visited[x][y] + 1
            queue.append((x, y+1))

    return visited

N, M = map(int, sys.stdin.readline().split())
Map = []

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    Map.append([int(num) for num in tmp])

result = mazeOpt(N, M, Map, (0, 0))
# for i in range(N):
#     print(result[i])
print(result[N-1][M-1])