# 큰 수의 법칙
import sys

N, M, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort(reverse=True)

print(((L[0] * K) + L[1]) * (M // (K + 1)) + L[0] * (M % (K + 1)))
