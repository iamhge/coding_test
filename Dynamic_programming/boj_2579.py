# 계단 오르기
'''
참고 : https://sungmin-joo.tistory.com/18?category=851625
'''
import sys

N = int(sys.stdin.readline().rstrip())
stair = [0]
dp = [0]

for _ in range(N):
    stair.append(int(sys.stdin.readline().rstrip()))

dp.append(stair[1])
if N >= 2: # N = 1일 경우 save
    dp.append(max(stair[1], stair[1] + stair[2]))

for i in range(3, N + 1):
    # i번째 stair까지 1칸 1칸 오른 경우 vs 2칸 1칸 오른 경우
    dp.append(max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i]))

print(dp[N])