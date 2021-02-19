# 2×n 타일링 2
'''
(i번째 방법) = (i-2번째 방법의 뒤에 1×2 타일 두개 붙인 것) 
                + (i-2번째 방법의 뒤에 2×2 타일 하나 붙인 것) 
                + (i-1번째 방법의 뒤에 2×1 타일 하나 붙인 것)
'''
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0]*(N+1)

for i in range(N+1):
    if i < 2:
        dp[i] = 1
        continue
    # 문제에서 하란대로 10007 나눈 나머지를 저장해야함.
    # 나중에 print할 때 한번에 나머지 연산하면 dp배열에 저장 시 너무 용량 커짐.
    dp[i] = (dp[i-2]*2 + dp[i-1])%10007

print(dp[N])