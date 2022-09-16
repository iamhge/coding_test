# 줄 서는 방법
# 2차시
'''
<풀이 방법>
  - a_1 = (k + (n-1)) // n
    a_2 ~ a_n 의 개수 = (n-1)!
  - a_1을 구한 후, a_2 ~ a_n 에서의 a_1을 다시 구하는 것을 반복한다.
    a_1을 구한 후 다음 k = (k + (factorial(n)) // (n) - 1) % ((factorial(n)) // (n) ) + 1
'''
fact = []

def factorial(n):
    global fact
    if fact[n] != 1 or n <= 1:
        return fact[n]
    
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i
    return fact[n]

def solution(n, k):
    global fact 
    fact = [1] * (n+1)
    
    numbers = [i for i in range( n+1)]
    answer = []
    remain = n
    
    for _ in range(n):
        divide = factorial(remain) // remain
        
        nextPerson = (k + divide-1) // divide
        answer.append(numbers.pop(nextPerson))
        
        k = (k + divide - 1) % divide + 1
        remain -= 1
        
    
    return answer

# 1차시
# 오답 2) 런타임 에러
'''
문제 풀이 실패
  사유) 런타임 에러를 못 고침
<풀이 방법>
  - 각 위치마다의 인덱스를 구하면서 줄을 세워간다.
  - k번째 방법의 i번째 사람의 번호는
    남은 사람들로 줄을 세우는 경우의 수 (n-i)! 중, k - (i-1번째 사람까지 세웠을 때의 경우의 수) 번째 이다.
    ex) k번째 방법에서 1번째 사람의 번호 = (k-1) // (n-1)! 번째 우선순위를 가지는 번호
  - priority : 우선순위로 나열된 남은 사람의 번호

런타임 에러 상황
  - n == 13
'''
import math

def solution(n, k): 
    answer = []
    priority = [i for i in range(1, n+1)]
    k -= 1
    for i in range(n-1, -1, -1):
        iFac = math.factorial(i)
        answer.append(priority[k//iFac])
        del priority[k//iFac]
        k = k % iFac
    return answer

# 오답 1) 시간 초과
'''
<풀이 방법>
  - 모든 경우의 수를 구한 후 정렬한다.
'''
'''
from itertools import permutations
def solution(n, k):
    return sorted(list(permutations([i for i in range(1, n+1)])))[k-1]
'''