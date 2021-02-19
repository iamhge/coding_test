# 오르막 수
'''
_ _ ... _ 0 뒤에 0~9 올 수 있음.( _ : i-1 개 )
_ _ ... _ 1 뒤에 1~9 올 수 있음.
_ _ ... _ 2 뒤에 2~9 올 수 있음.
.
.
.
_ _ ... _ 9 뒤에 9 올 수 있음.

=> i-1 자리수를 갖는 오르막수의 1의 자리에 따라, 
i 자리수를 갖는 오르막수의 1의 자리에 올 수 있는 수가 달라짐.

'''
import sys

N = int(sys.stdin.readline().rstrip())
# dp[n] = 1의 자리가 n인 수의 개수
dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
tmp = [[0]*10]

for i in range(2, N+1):
    tmp = dp
    dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(10):
        for k in range(j, 10):
            dp[k] += tmp[j]

print(sum(dp)%10007)

# 메모리 10배 많이 쓴 답안(맞는 답이긴 함)
'''
import sys

N = int(sys.stdin.readline().rstrip())
dp = [[0]*10 for _ in range(N+1)]
# dp[m][n] = 길이가 m인 오르막 수 중 1의 자리가 n인 수의 개수
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][k] += dp[i-1][j] 

print(sum(dp[N])%10007)
'''