def solution(enroll, referral, seller, amount): # referral[i] = enroll[i]의 부모
    # root 추가
    enroll.append('-')
    result = [0] * len(enroll)
    
    # 빠른 탐색을 위해 dictionary로 재구성한다.
    myenroll = {}
    for i, e in enumerate(enroll):
        myenroll[e] = i
    
    # referral에 이름이 아닌 구성원의 index를 저장한다.
    myreferral = [0] * len(referral)
    for i, r in enumerate(referral):
        myreferral[i] = myenroll[r]
    
    for i, s in enumerate(seller):
        money = amount[i]*100
        
        # seller의 index
        si = myenroll[s]
        
        while si < len(enroll)-1:
            # result[si] += money*9//10 # 이렇게 하면 올림이 안되므로 아래와 같이 연산해야함.
            result[si] += money - money//10
            money //= 10
            
            # 10%를 계산한 금액이 1원 미만인 경우
            if money < 1:
                result[si] += money
                break;
        
            # 부모의 index
            si = myreferral[si]
        
    return result[:-1]

# 시간 초과
'''
from collections import defaultdict

def solution(enroll, referral, seller, amount): # referral[i] = enroll[i]의 부모
    enroll.append('-')
    result = [0] * len(enroll)
    
    for i in range(len(seller)):
        # seller의 index
        si = enroll.index(seller[i])
        money = amount[i]*100
        
        while enroll[si] != '-':
            # result[si] += money*9//10 # 이렇게 하면 올림이 안되므로 아래와 같이 연산해야함.
            result[si] += money - money//10
            money //= 10
            
            # 10%를 계산한 금액이 1원 미만인 경우
            if money < 1:
                result[si] += money
                break;
        
            # 부모의 si
            si = enroll.index(referral[si])
        
    return result[:-1]
'''