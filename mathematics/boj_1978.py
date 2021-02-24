# 소수 찾기
import sys
import math

def isPrimeNumber(num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().split()))
result = 0

for x in X:
    if isPrimeNumber(x):
        result += 1

print(result)

# 참고
# https://boycoding.tistory.com/225 

# 다른 사람 코드
'''
def prime(a):
    if a < 2: # 1
        return 0 
    i = 2
    while i*i <= a: # i의 제곱 사이의 값들에 i를 나눴을 때..
        if a % i == 0:
            return 0
        i += 1
    return 1 # 2, 3은 while문 통과
'''