# 좌표 정렬하기
import sys

N = int(sys.stdin.readline().rstrip())
coordinate = []
for _ in range(N):
    coordinate.append(tuple(map(int, sys.stdin.readline().split())))

for x, y in sorted(coordinate):
    print(x, y)