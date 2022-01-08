# 큰 수 만들기

def myIndexOfMax(array):
    maxNum = "0"
    result = 0
    for i in range(len(array)):
        if array[i] > maxNum:
            maxNum = array[i]
            result = i
        if maxNum == "9":
            break
    return result

def solution(number, k):
    m = len(number) - k
    answer = ""
    
    for i in range(m, 0, -1):
        n = len(number)
        indexOfMax = myIndexOfMax(number[:n-i+1])
        answer += number[indexOfMax]
        number = number[indexOfMax+1:]
    
    return answer

# 시간 초과 1
'''
<풀이 방법>
  - 모든 조합을 구한 후, 그 중 가장 큰 값을 구한다.
  - 파이썬 내장 함수인 itertools를 사용한다.
'''
'''
from itertools import combinations

def solution(number, k):    
    combi = list(int("".join(cb)) for cb in combinations(number, len(number) - k))
    return str(max(combi))
'''

# 시간 초과 2
'''
<풀이 방법>
  - 모든 조합을 구한 후, 그 중 가장 큰 값을 구한다.
  - 직접 Combinations함수를 구현한다.
'''
'''
import sys
sys.setrecursionlimit(1000000) # 안해주면 런타임 에러 발생

def myCombinations(array, m):
    result = []
    n = len(array)
    
    if m == 1:
        return list(array)
    for i in range(n-m+1):
        combis = myCombinations(array[i+1:], m-1)
        for combi in combis:
            result.append(array[i] + combi)
    
    return result

def solution(number, k):
    return str(max(list(map(int, myCombinations(number, len(number) - k)))))
'''

# 시간 초과 3
'''
<풀이 방법>
  - 모든 조합을 구한 후, 그 중 가장 큰 값을 구한다.
  - 직접 Combinations함수를 구현한다.
'''
'''
import sys
sys.setrecursionlimit(1000000) # 안해주면 런타임 에러 발생

def myCombinations(array, m):
    result = []
    n = len(array)
    first = max(list(array[:n-m+1]))
    
    if m == 1:
        return list(array)
    for i in range(n-m+1):
        if array[i] != first:
            continue
        combis = myCombinations(array[i+1:], m-1)
        for combi in combis:
            result.append(array[i] + combi)
    
    return result

def solution(number, k):
    return str(max(list(map(int, myCombinations(number, len(number) - k)))))
'''

# 시간 초과 4
'''
<풀이 방법>
  - 모든 조합을 구한 후, 그 중 가장 큰 값을 구한다.
  - Greedy 알고리즘을 사용한다.
  - recursion으로 찾는다.
'''
'''
import sys
sys.setrecursionlimit(1000000) # 안해주면 런타임 에러 발생

def findMax(array, m):
    if m == 1:
        return max(list(array))
    
    n = len(array)
    maxNum = max(list(array[:n-m+1])) # array의 뒤에서부터 m-1개를 제외하고 가장 큰 숫자
    
    for i in range(n-m+1):
        if array[i] == maxNum:
            return array[i] + findMax(array[i+1:], m-1)
        
def solution(number, k):
    return findMax(number, len(number) - k)
'''

# 실패 + 시간 초과
'''
import sys
sys.setrecursionlimit(1000000) # 안해주면 런타임 에러 발생

def findMax(array, m):
    if m == 1:
        return max(list(array))
    
    n = len(array)
    maxNum = max(list(array[:n-m+1])) # array의 뒤에서부터 m-1개를 제외하고 가장 큰 숫자
    
    for i in range(n-m+1):
        if array[i] == maxNum:
            return array[i] + findMax(array[i+1:], m-1)
        
def findMin(array, m):
    if m == 1:
        return min(list(array))
    
    n = len(array)
    minNum = min(list(array[:n-m+1])) # array의 뒤에서부터 m-1개를 제외하고 가장 작은 숫자
    
    for i in range(n-m+1):
        if array[i] == minNum:
            return array[i] + findMin(array[i+1:], m-1)
        
def solution(number, k):
    if len(number)//2 >= k:
        return findMax(number, len(number) - k)
    else:
        answer = ""
        minNum = findMin(number, k)
        for i in range(len(number)):
            if len(minNum) == 0:
                answer += number[i:]
                break
            if number[i] == minNum[0]:
                minNum = minNum[1:]
            else:
                answer += number[i]
        return answer
'''

# 시간초과 5
'''
<풀이 방법>
  - 모든 조합을 구한 후, 그 중 가장 큰 값을 구한다.
  - Greedy 알고리즘을 사용한다.
  - recursion으로 찾는다.
'''
'''
import sys
sys.setrecursionlimit(1000000) # 안해주면 런타임 에러 발생

def myIndexOfMax(array):
    maxNum = "0"
    result = 0
    for i in range(len(array)):
        if array[i] > maxNum:
            maxNum = array[i]
            result = i
        if maxNum == "9":
            break
    return result

def myMax(array):
    maxNum = "0"
    
    for i in range(len(array)):
        if array[i] > maxNum:
            maxNum = array[i]
        if maxNum == "9":
            return "9"
    return maxNum

def findMax(array, m):
    if m == 1:
        return myMax(array)
    n = len(array)
    indexOfMax = myIndexOfMax(array[:n-m+1]) # array의 뒤에서부터 m-1개를 제외하고 가장 큰 숫자의 인덱스
    return array[indexOfMax] + findMax(array[indexOfMax+1:], m-1)

def solution(number, k):
    return findMax(number, len(number) - k)
'''