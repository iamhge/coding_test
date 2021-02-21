# 단지번호붙이기
import sys
from collections import deque

def BFS(M: list, root: tuple):
    visited = []
    queue = deque([root])
    aptNum = 0

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n[0] != 0 and M[n[0]-1][n[1]]: # 상
                queue.append((n[0]-1, n[1]))
            if n[0] != N-1 and M[n[0]+1][n[1]]: # 하
                queue.append((n[0]+1, n[1]))
            if n[1] != 0 and M[n[0]][n[1]-1]: # 좌
                queue.append((n[0], n[1]-1))
            if n[1] != N-1 and M[n[0]][n[1]+1]: # 우
                queue.append((n[0], n[1]+1))
            M[n[0]][n[1]] = 0
            aptNum += 1
    return aptNum

N = int(sys.stdin.readline().rstrip())
Map = []
aptNum = []
complexNum = 0

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    Map.append([int(num) for num in tmp])

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            aptNum.append(BFS(Map, (i, j)))
            complexNum += 1

print(complexNum)
for num in sorted(aptNum):
    print(num)