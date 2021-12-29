# 다음 큰 숫자

# 내 코드
# 2진수로 변환했을 때의 1의 개수
def binaryOneCount(n):
    result = 0

    while n >= 1:
        if n % 2 == 1:
            result += 1
        n //= 2
        
    return result

def solution(n):
    oneCount = binaryOneCount(n)
    
    while 1:
        n += 1
        if oneCount == binaryOneCount(n):
            break
    
    return n

# 다른 사람 코드
'''
파이썬 자체의 binary 함수와 count 함수를 사용해 구현.
'''
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n