# 숫자 블록
# 다른 사람 코드 참고
'''
<풀이 방법>
  - 본인을 제외하고 최대의 약수에 해당한다.
<참고>
  [프로그래머스] 숫자블록 파이썬 풀이
  : https://velog.io/@rltjr1092/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90%EB%B8%94%EB%A1%9D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4
<소감>
  - binary search 넣구 막 어렵게 생각했는데, 풀이는 너무 쉬워서 속상하다...
'''
def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        for j in range(2, int(i**0.5)+1): # i**0.5 == sqrt(i)
            if i % j == 0 and i // j <= 10000000:
                answer.append(i // j)  # j가 2부터 커지기 때문에 처음 만나는 i//j가 약수 중 가장 큰 값
                break
        else:
            answer.append(1)
    return answer

'''
from math import sqrt
primes = []

def binarySearch(target):
    start = 1
    result = 1
    end = int(sqrt(target)) + 1
    
    if target == 1: return 0
    while start <= end:
        mid = (start + end) // 2
        
        if target % mid == 0:
            if isPrimeNum(mid):
                result = target // mid
            end = mid - 1
        elif target // mid == 0:
            end = mid - 1
        else:
            start = mid + 1
    return result
    
# 소수인지 아닌지 반환한다.
def isPrimeNum(n):
    global primes
    if n in primes:
        return True
    
    if n <= 1: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    primes.append(n)
    return True

def solution(begin, end):
    answer = []
    prime = []
    
    for i in range(begin, end+1):
        answer.append(binarySearch(i))
    
    return answer
'''
# 마찬가지로 시간 초과
'''
from math import sqrt

# 소수인지 아닌지 반환한다.
def isPrimeNum(n):
    if n <= 1: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(begin, end):
    primes = []
    answer = []
    maxiP = min(end+1, 10000001)
    numbers = [True] * maxiP # prime num 인지 아닌지
    numbers[1] = False
    
    for i in range(2, maxiP):
        if not numbers:
            continue
        if isPrimeNum(i):
            primes.append(i)
            j = 0
            while i*j < maxiP:
                numbers[i*j] = False
                j += 1
    print(primes)
    
    for i in range(begin, end+1):
        if i == 1: answer.append(0)
        elif not numbers[i]:
            for p in primes:
                if i % p == 0:
                    answer.append(i // p)
                    break
        else:
            answer.append(i)
    
    return answer
'''
# 시간 초과
'''
<풀이 방법>
  - 본인을 제외하고 최대의 약수에 해당한다.
     = 약수 중 가장 작은 소수로 나눈 수
<오답 노트>
  - 소수 검사를 모두 시행해서, 효율성 검사 망할거라 예상하긴 했지만 역시는 역시나 역시였다.
'''
'''
from math import sqrt

def isPrimeNum(n):
    if n <= 1: return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return n // i
    return 1
    
def solution(begin, end):
    answer = []
    prime = []
    for i in range(begin, end+1):
        answer.append(isPrimeNum(i))
    
    return answer
'''