# k진수에서 소수 개수 구하기
import re

def kNumeral(n, k):
    result = ''
    while n >= 1:
        result += str(n % k)
        n //= k
    return result[::-1]

def isPrimeNumber(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    for num in re.split('[0]+', kNumeral(n, k)):
        if num == '': continue
        if isPrimeNumber(int(num)):
            answer += 1
        
    return answer