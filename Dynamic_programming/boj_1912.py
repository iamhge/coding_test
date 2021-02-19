# 연속합
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
dp = [0]*N
dp[0] = A[0]
for i in range(1, N):
    dp[i] = max(dp[i-1] + A[i], A[i])

print(max(dp))