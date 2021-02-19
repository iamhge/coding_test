# 1로 만들기
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    # 2로 나누어 떨어질 경우와 3으로 나누어 떨어질 경우 모두를 고려해야함.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])

# 처음에 제출하고 틀린 코드
'''
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0]*(N+1)

for i in range(2, N+1):
    if i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    elif i % 2 == 0: # 이렇게 elif로 하면 안됨!
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        dp[i] = dp[i-1] + 1
        
print(dp[N])
'''