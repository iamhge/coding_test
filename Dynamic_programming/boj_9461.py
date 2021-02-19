# 파도반 수열
'''
그냥 피보나치 변형
'''
import sys

T = int(sys.stdin.readline().rstrip())
N = [0 for _ in range(T)]

for i in range(T):
    N[i] = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(max(N) + 1)]

for i in range(max(N)+1):
    if i <= 3:
        dp[i] = 1
        continue
    dp[i] = dp[i-3] + dp[i-2]

for n in N:
    print(dp[n])