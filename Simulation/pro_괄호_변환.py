# 괄호 변환
'''
<문제 이해 참고>
  - https://programmers.co.kr/questions/8183
'''
from collections import deque

def isCorrect(p):
    stack = deque([p[0]])
    for i in range(1, len(p)):
        if p[i] == ")":
            if len(stack) == 0: return False
            stack.pop()
        else:
            stack.append("(")
    if len(stack) != 0: return False
    return True

def isBalanced(p):
    if p.count('(')*2 == len(p):
        return True
    else:
        return False
    
def converse(u):
    converseBase = {'(': ')', ')': '('}
    return ''.join([converseBase[c] for c in u])

def makeCorrect(p):
    answer = ''
    
    # 1
    if p == '':
        return ''
    # 2
    i = 1
    while not isBalanced(p[:i]):
        if i == len(p): break
        i += 1
    u = p[:i]
    v = p[i:]
    # 3
    if isCorrect(u):
        answer += u
        answer += makeCorrect(v)
    # 4
    else:
        answer += '(' + makeCorrect(v) + ')' + converse(u[1:-1])
    
    return answer

def solution(p):
    answer = ''
    if isCorrect(p): return p
    return makeCorrect(p)