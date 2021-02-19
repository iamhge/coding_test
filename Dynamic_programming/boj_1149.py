# RGB거리
'''
참고 : https://chunghyup.tistory.com/48
어렵다.. 짱난다...
'''
import sys

N = int(sys.stdin.readline().rstrip())
RGB = []
dp = [[0]*3 for _ in range(N)]

for i in range(N):
    RGB.append(list(map(int, sys.stdin.readline().split())))

dp[0] = RGB[0]

for i in range(1, N):
    dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])


print(min(dp[N-1]))