# 음료수 얼려 먹기
'''
<입력 예시>
4 5
00110
00011
11111
00000
-> 3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
-> 8
'''
import sys
from collections import deque

input = sys.stdin.readline

def DFS(N: int, M: int, Map: list, root: tuple):
    stack = deque([root])

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while stack:
        y, x = stack.pop()
        Map[y][x] = -1 # visited

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] == 0:
                stack.append([ny, nx])

N, M = map(int, input().split())
Map = []
for _ in range(N):
    Map.append([int(i) for i in list(input().rstrip())])

count = 0

for i in range(N): # 행
    for j in range(M): # 열
        if Map[i][j] == 0:
            DFS(N, M, Map, (i, j))
            count += 1

print(count)