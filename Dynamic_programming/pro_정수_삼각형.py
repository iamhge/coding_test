# 정수 삼각형
def solution(triangle):
    dp = triangle[:]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
                
    return max(dp[-1])