'''
1) 0번째 집을 털 경우 -> 마지막 집을 털지 못함
2) 0번째 집을 털지 않을 경우 -> 마지막 집을 털 수 있음
dp[i] = i번째 집에서 벌 수 있는 돈의 최댓값
      = max(dp[i-2] + money[i], dp[i-1])
'''

def solution(money):
    answer = 0
    house = len(money)
    dp = [0] * house
    dp2 = [0] * house
    # 1) 0번째 집 털고, 마지막 집 털지 않는다.
    dp[0] = money[0]
    dp[1] = money[0]
    for i in range(2, house-1):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    dp[-1] = dp[-2]
    
    # 2) 0번째 집 털지 않고, 마지막 집은 털던가 말던가~
    dp2[1] = money[1]
    for i in range(2, house):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
    
    return max(max(dp), max(dp2))