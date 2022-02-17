# 2 x n 타일링
'''
<문제 정보>
  - boj_11726.py(백준 11726 - 2xn 타일링)과 같은 문제
  - 복습
'''
def solution(n):
    dp = [0] * (n+1)

    for i in range(1, n+1):
        if i <= 2:
            dp[i] = i
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n] 