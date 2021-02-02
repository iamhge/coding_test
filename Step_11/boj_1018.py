# 체스판 다시 칠하기
import sys

N, M = map(int, sys.stdin.readline().split())
chess = [[]*M]*N

for i in range(N):
    chess[i] = list(sys.stdin.readline().rstrip())

minColoring = N*M

for i in range(N-7):
    for j in range(M-7):
        coloring = 0
        start = chess[i][j]
        for k in range(8): 
            for l in range(8):
                if (k + l)%2 == 0 and chess[i+k][j+l] != start:
                    coloring += 1
                elif (k + l)%2 == 1 and chess[i+k][j+l] == start:
                    coloring += 1
        # start를 바꾼 경우가 더 효율적일 수 있으므로 min적용
        if min(64 - coloring, coloring) < minColoring:
            minColoring = min(64 - coloring, coloring)

print(minColoring)