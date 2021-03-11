# 안전 영역
'''
<아이디어>
  * BFS로 영역의 수를 세어주면 되는 간단한 문제
  * 
<문제 해석>
  * 안전한 영역 : '영역'을 말하는 것이므로, 안전한 위치의 개수가 아님 주의.
  * 높이에 따라서 안전한 영역의 수가 다르므로, 모든 높이를 순회해서 
    안전한 영역이 최대일 때를 찾아야 함.
'''
import sys
from collections import deque

input = sys.stdin.readline

def BFS(N: int, M: list, root: tuple, h: int, safeZone: list, numOfSZ: int) -> list:
    visited = [[False]*N for _ in range(N)]
    queue = deque([root])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True
        safeZone[y][x] = numOfSZ

        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < N and 0 <= y_ < N:
                if h < M[y_][x_]:
                    queue.append((x_, y_))
                    
    return safeZone

def main():
    N = int(input().rstrip())
    M = []
    for _ in range(N):
        M.append(list(map(int, input().split())))

    mini = min(map(min, M)) - 1
    maxi = max(map(max, M))
    result = 1

    for h in range(mini, maxi):
        safeZone = [[0]*N for _ in range(N)]
        numOfSZ = 0
        for y in range(N):
            for x in range(N):
                if h < M[y][x] and safeZone[y][x] == 0:
                    numOfSZ += 1
                    safeZone = BFS(N, M, (x, y), h, safeZone, numOfSZ)  
                    # for i in range(N):
                    #     print(safeZone[i])
                    # print()  
                result = max(numOfSZ, result)
    
    print(result)

if __name__ == "__main__":
    main()