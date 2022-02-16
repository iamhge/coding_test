# 멀리 뛰기
'''
<풀이 방법>
  다이나믹 프로그래밍
  - an = (an-1 뒤에 1칸을 뛸 경우) + (an-2 뒤에 2칸을 뛸 경우)
'''

def solution(n):
    if n <= 2: return n
    
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567