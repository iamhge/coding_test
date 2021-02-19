# 평범한 배낭
'''
참고 : https://devjin-blog.com/boj-12865-knapsack/ 
test)
4 10
5 10
4 40
6 30
3 50
-> 90
'''
import sys

N, K = map(int, sys.stdin.readline().split())
item = [[0]*2 for _ in range(N+1)]
dp = [0]*(K + 1)

for i in range(1, N+1):
    item[i][0], item[i][1] = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    for k in range(K, 1, -1): # 뒤로 가는 것 기억할 것
        if item[i][0] <= k:
            dp[k] = max(dp[k - item[i][0]] + item[i][1] , dp[k])
            # print(dp)

print(dp[K])

# 시간 초과
'''
for i in range(1, N+1):
    for k in range(1, K+1):
        # i번째 item의 무게를 더해도 배낭에 들어갈 때
        if k >= W[i-1][k] + item[i][0]:
            V[i][k] = V[i-1][k] + item[i][1]
            W[i][k] = W[i-1][k] + item[i][0]
        elif k >= item[i][0]:
            if V[i-1][k - item[i][0]] + item[i][1] > V[i-1][k]:
                V[i][k] = V[i-1][k - item[i][0]] + item[i][1]
                W[i][k] = W[i-1][k - item[i][0]] + item[i][0]
            else:
                V[i][k] = V[i-1][k]
                W[i][k] = W[i-1][k]
        elif k >= W[i-1][k]:
            V[i][k] = V[i-1][k]
            W[i][k] = W[i-1][k]

print(V[N][K])
'''