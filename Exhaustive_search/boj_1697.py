# 숨바꼭질
# BFS 공부하고 다시오자~~
# 7번 틀린 코드^^ 욕나온당
import sys

N, K = map(int, sys.stdin.readline().split())
dp = [100000]*100003

for i in range(K+2):
    dp[i] = min(dp[i], abs(N-i))

    if i % 2 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i//2] + 1, dp[i])
    else:
        dp[i] = min(dp[i-1] + 1, dp[i])

    if i != 0:
        dp[i-1] = min(dp[i] + 1, dp[i-1])
    dp[i+1] = min(dp[i] + 1, dp[i+1])

print(dp[K])