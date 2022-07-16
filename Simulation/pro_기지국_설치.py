# 기지국 설치
'''
- 해설 보고 풀이
<참고>
  - 해설 : https://school.programmers.co.kr/questions/27785
'''
def solution(n, stations, w):
    answer = 0
    stations.sort()
    
    if stations[0] > w+1:
        answer += (stations[0] - (w+1) + 2*w) // (2*w + 1)

    for i in range(1, len(stations)):
        answer += (stations[i] - stations[i-1] - 1) // (2*w + 1)
    
    if n - stations[-1] > w:
        answer += (n - (stations[-1] + w) + 2*w) // (2*w + 1)
    
    return answer

# 틀린 풀이
'''
<풀이 방법>
  Dynamic Programming (DP)
  - a_k = 현재까지 기지국의 개수
  - a_k = 
        if (a_k-2w-1) == a_k-1: a_k += 1
        else: a_k += a_k-1
'''
'''
def solution(n, stations, w):
    answer = 0
    dp = [0] * (n+1)
    
    for station in stations:
        dp[station] += 1
        
    for i in range(1, w+2):
        if i in stations:
            dp[i] = 1
            
    else:
        
    for i in range(2, 2*w+2):
        if i in stations:
            dp[i] += dp[i-1]
        elif dp[1] != dp[i-1]:
            dp[i] = dp[i-1]
    
    for i in range(2*w+2, n+1):
        if i in stations: # 이미 설치된 기지국인 경우
            dp[i] += dp[i-1]
        elif dp[i-(2*w+1)] == dp[i-1]: 
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return dp[n] - len(stations)
'''