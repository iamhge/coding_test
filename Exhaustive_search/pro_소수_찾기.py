# 소수 찾기
'''
<참고>
  코딩테스트를 위한 파이썬 문법 (5) (built-in functions, itertools)
   : https://velog.io/@janeljs/python-for-coding-test-5
'''
from itertools import permutations

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    nums = set(int(num) for num in numbers)
    
    for i in range(2, len(numbers)+1):
        nums |= set(int("".join(pm)) for pm in permutations(numbers, i))
    
    count = 0
    for num in nums:
        if isPrime(num):
            count += 1
    
    return count