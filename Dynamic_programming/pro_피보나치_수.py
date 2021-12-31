# 피보나치 수
def solution(n):
    a = 0 # F(n-2)
    b = 1 # F(n-1)
    
    for i in range(2, n+1):
        tmp = a
        a = b
        b += tmp

    return b % 1234567