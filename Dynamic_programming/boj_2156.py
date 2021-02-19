# 포도주 시식
# 참고 : https://in0-pro.tistory.com/26
# 첨에 꼭 i번째 잔을 비워야한다고 생각해서 틀림.
import sys

n = int(sys.stdin.readline().rstrip())
dp = [0]*(n+1)
wine = [0]

for _ in range(n):
    wine.append(int(sys.stdin.readline().rstrip()))

dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    # i-2번째 잔을 마시지 않고 i-1, i번째 잔을 비우는 경우
    # vs i-2, i번째 잔을 비우는 경우 
    # vs i번째 잔을 마시지 않는 경우(i-1의 dp)
    dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

print(dp[n])

# 처음에 낸 오답
'''
import sys

n = int(sys.stdin.readline().rstrip())
dp = [0]*(n+1)
wine = [0]

for _ in range(n):
    wine.append(int(sys.stdin.readline().rstrip()))

dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    # i-3, i-1, i번째 잔을 비우는 경우 vs i-3, i-2, i번째 잔을 비우는 경우
    dp[i] = dp[i-3] + max(wine[i-1], wine[i-2]) + wine[i]

print(dp[n])
'''