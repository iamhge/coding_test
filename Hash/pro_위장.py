# 위장
def solution(clothes):
    answer = 1
    count = {} # 옷의 종류 : 개수
    
    for cloth in clothes:
        if cloth[1] in count:
            count[cloth[1]] += 1
        else:
            count[cloth[1]] = 1

    for value in count.values():
        answer *= (value + 1) # +1 : 해당 종류의 옷을 입지 않는 경우 포함

    answer -= 1 # -1 : 옷을 하나도 입지않는 경우
    
    return answer