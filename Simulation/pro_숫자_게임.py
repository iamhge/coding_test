# 숫자 게임
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    i = 0
    
    for b in B:
        if A[i] >= b: continue
        answer += 1
        i += 1
    
    return answer