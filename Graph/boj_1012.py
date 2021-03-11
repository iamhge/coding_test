# 유기농 배추
import sys
from collections import deque

def DFS(M: int, N: int, Map: list, root: tuple, count: int):
    visited = []
    stack = deque([root])
    dx = [0, 0, -1, 1] # 상하좌우
    dy = [-1, 1, 0 ,0]

    while stack:
        x, y = stack.pop()

        if (x, y) not in visited:
            visited.append((x, y))
            Map[y][x] = count
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0 <= x_ < M and 0 <= y_ < N and Map[y_][x_] == 1:
                    stack.append((x_, y_))
                    
    return Map
 
def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        Map = [[0]*M for __ in range(N)]
        count = 2
        for __ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            Map[Y][X] = 1
        for i in range(N): # y
            for j in range(M): # x
                if Map[i][j] == 1:
                    Map = DFS(M, N, Map, (j, i), count)
                    count += 1
        # for i in range(N):
        #     print(Map[i])
        print(max(map(max, Map))-1)

if __name__=="__main__":
    main()