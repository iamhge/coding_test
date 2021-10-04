# 숫자 카드 게임
import sys

N, M = map(int, sys.stdin.readline().split())
result = 0

for i in range(N):
    result = max(result, min(list(map(int, sys.stdin.readline().split()))))

print(result)