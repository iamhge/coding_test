# 주식가격
'''
<내 풀이>
  - stack, queue가 아닌 것 같음.
  - 단순 Exhaustive search
'''
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]: # 떨어지면
                break
    
    return answer