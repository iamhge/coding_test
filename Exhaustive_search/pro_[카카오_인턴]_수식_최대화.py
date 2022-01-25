# [카카오 인턴] 수식 최대화
'''
<풀이 방법>
  - 완전 탐색 : 모든 연산 순서에 따른 결과를 반환한다.
'''
from itertools import permutations
import copy

# *, -, + 계산
def calculate(a, b, op):
    if op == '*':
        return a * b
    elif op == '-':
        return a - b
    elif op == '+':
        return a + b

# N개의 연산자의 우선 순위에 따라 연산 수행
def opN(nums, ops, ps):
    tmpNums, tmpOps = copy.deepcopy(nums), copy.deepcopy(ops)
    for p in ps:
        tmpNums, tmpOps = op1(tmpNums, tmpOps, p)
    return tmpNums[0]

# p 연산자에 대한 연산만 수행
def op1(nums, ops, p):
    tmpNums = copy.deepcopy(nums)
    newNums = []
    newOps = []
    i = 0
    while i < len(ops):
        while ops[i] == p:
            tmpNums[i+1] = calculate(tmpNums[i], tmpNums[i+1], ops[i])
            i += 1
        newNums.append(tmpNums[i])
        newOps.append(ops[i])
        i += 1
    return newNums, newOps

def solution(expression):
    answer = 0
    
    # nums와 ops에 각각 숫자와 연산자 리스트 만들기
    i = 0
    nums = ['']
    ops = []
    for e in expression:
        if e != '+' and e != '-' and e != '*':
            nums[i] += e
        else:
            ops.append(e)
            nums.append('')
            i += 1
    nums = list(map(int, nums))
    
    opCnt = len(set(ops)) # 연산자의 개수
    ops.append('=') # nums와 ops의 길이 맞춰주기 용
    
    if opCnt == 3: # 연산자가 3개인 경우
        seq = list(permutations(['*', '-', '+']))
        for ps in seq:
            answer = max(answer , abs(opN(nums, ops, ps)))
    elif opCnt == 2: # 연산자가 2개인 경우
        seq = list(permutations(set(ops[:-1])))
        for ps in seq:
            answer = max(answer , abs(opN(nums, ops, ps)))
    else: # 연산자가 1개인 경우
        answer = abs(opN(nums, ops, (ops[0])))
    
    return answer

# 다른 사람 코드
'''
<구현 방식>
  - 정규표현식 사용
    - re : 정규 표션식 모듈
    - r'(\D)' : 정규 표현식
      - r : raw string으로 백슬래시 문자를 해석하지 않고 남겨두는 것
            만약 r없이 사용한다면 '(\\D)' 과 같이 백슬래시에 백슬래시를 넣어줘야 한다.\
      - \D : 숫자가 아닌 것에 대한 정규표현식
    - re.split : 문자열에서 패턴이 맞으면 이를 기점으로 쪼갠다.
      - r'(\D)'의 () : 해당 분리 문자도 결과 문자열에 포함한다.
  - eval 함수 사용
    : 매개변수로 받은 expression을 문자열로 받아서 실행한다.
<참고>
  - 07-2 정규 표현식 시작하기
    : https://wikidocs.net/4308
  - [Python] re 모듈 사용법
    : https://brownbears.tistory.com/506
  - 파이썬 - 정규식표현식(Regular Expression) 모듈
    : https://devanix.tistory.com/296
'''
'''
import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)
'''