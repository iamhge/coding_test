# 스티커 모으기(2)
'''
<풀이 방법>
 Dynamic Programming (DP)
 - ak = (sticker[:k+1]의 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값)
 - ak = max(ak-2 + sticker[k], ak-1)
 - but, 원형 스티커이기 때문에 특수한 경우다.
   따라서 0번째 스티커를 떼는가, 떼지 않는가로 나누어 계산한다.
'''
def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    
    # 1. 0번째 스티커를 떼는 경우
    dp = [0] * len(sticker)
    
    dp[0] = dp[1] = sticker[0]
    
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    
    dp[-1] = dp[len(sticker)-2]
    
    # 2. 0번째 스티커를 떼지 않는 경우
    dp2 = [0] * len(sticker)
    
    dp2[1] = sticker[1]
    
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])

    return max(dp[-1], dp2[-1])