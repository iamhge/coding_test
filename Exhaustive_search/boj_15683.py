# 감시
'''
<아이디어>
  * 단순한 브루트포스
    CCTV가 최대 8개이므로 완전탐색으로도 충분하다.
'''
import sys
from collections import deque
input = sys.stdin.readline


def DFS(N, M, Map, dx, dy, root):
    stack = deque([root])
    ret = 0
    
    while stack:
        x, y = stack.pop()
        x = x + dx
        y = y + dy
        if x >= M or x < 0 or y >= N or y < 0 or Map[y][x] == 6:
            return Map, ret
        elif Map[y][x] == 0:
            Map[y][x] = '#'
            ret += 1
        stack.append((x, y))

    return Map, ret

def main():
    N, M = map(int, input().split())
    Map = []

    dx = [0, 1, -1, 0] # 시계방향 상 우 하 좌
    dy = [-1, 0, 0, 1]

    for _ in range(N):
        Map.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 5:
                for k in range(4):
                    Map, res = DFS(N, M, Map, dx[k], dy[k], (i, j))
            elif Map[i][j] == 4:
                for k in range(4):
                    Map, tmp[0] = DFS(N, M, Map, dx[k], dy[k], (i, j))
                    Map, tmp[1] = DFS(N, M, Map, dx[k-1], dy[k-1], (i, j))
                    Map, tmp[2] = DFS(N, M, Map, dx[k-2], dy[k-2], (i, j))
                    
            elif Map[i][j] == 3:
                for k in range(4):
                    Map, tmp = DFS(N, M, Map, dx[k], dy[k], (i, j))
                    Map, tmp = DFS(N, M, Map, dx[k-1], dy[k-1], (i, j))
            elif Map[i][j] == 2:
                for k in range(2):
                    Map, tmp = DFS(N, M, Map, dx[k], dy[k], (i, j))
                    Map, tmp = DFS(N, M, Map, dx[k-2], dy[k-2], (i, j))
            elif Map[i][j] == 1:
                for k in range(4):
                    Map, tmp = DFS(N, M, Map, dx[k], dy[k], (i, j))


if __name__=="__main__":
    main()