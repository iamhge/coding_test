# 1, 2, 3 더하기
'''
(i번째 방법) = (i-3번째 방법의 뒤에 3을 붙인 경우)
                + (i-2번째 방법의 뒤에 2를 붙인 경우)
                + (i-1번째 방법의 뒤에 1을 붙인 경우)
'''
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dp = [0]*(N+1)

    dp[0] = 1 # 실제로는 i = 0이 없지만 i = 3인 경우를 맞춰주기 위해 1 넣음.
    dp[1] = 1
    if N >= 2:
        dp[2] = 2

    for i in range(3, N+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[N])