# 평범한 배낭
import sys

N, K = map(int, sys.stdin.readline().split())
item = []
for _ in range(N):
    item.append(tuple(map(int, sys.stdin.readline().split())))

dp = [0]*(K+1)

for w, v in item:
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j-w] + v, dp[j])

print(dp[K])