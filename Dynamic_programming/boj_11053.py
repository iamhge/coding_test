# 가장 긴 증가하는 부분 수열
import sys

N = int(sys.stdin.readline().rstrip())
A = [0]
A.extend(list(map(int, sys.stdin.readline().split())))
dp = [1]*(N+1)

for i in range(2, N+1):
    for j in range(i, 0, -1):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])
    
print(max(dp))

# 다른 사람 코드
# https://pacific-ocean.tistory.com/153
# 자기 자신보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1
'''
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
'''