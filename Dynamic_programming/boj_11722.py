# 가장 긴 감소하는 부분 수열
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
dp = [1]*N

for i in range(N):
    for j in range(i, -1, -1):
        if A[j] > A[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))