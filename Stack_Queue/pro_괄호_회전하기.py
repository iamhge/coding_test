# 괄호 회전하기
'''
<풀이 방법>
  - 첫 문자를 stack에 넣는다.
  - stack의 문자와 다음 문자가 올바른 닫는 괄호라면 pop한다.
  - stack[-1]과 다음 문자가 올바른 짝이 아니라면 다음 문자를 스택에 넣는다.
    - 이 때 다음 문자는 여는 괄호여야한다.
    - 닫는 괄호라면 False
'''
from collections import deque
rule = '()[]{}'

def isPair(a, b):
    if rule[rule.find(b) - 1] == a:
        return True
    return False

def check(s):
    stack = deque()
    
    for c in s:
        if len(stack) == 0:
            if rule.find(c) % 2 == 0:
                stack.append(c)
            else:
                return False
        elif isPair(stack[-1], c):
            stack.pop()
        elif rule.find(c) % 2 == 0:
            stack.append(c)
        else:
            return False
        
    if len(stack) > 0:
        return False
    
    return True

def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return answer
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            answer += 1
    return answer

'''
<풀이 방법>
  - 첫 문자를 stack에 넣는다.
  - stack의 문자와 다음 문자가 올바른 닫는 괄호가 아니라면 다음 문자를 스택에 넣는다.
  - stack의 문자와 다음 문자가 올바른 닫는 괄호라면 pop한다.
'''
'''
from collections import deque
rule = '()[]{}'

def isPair(a, b):
    if rule[rule.find(b) - 1] == a:
        return True
    return False

def check(s):
    stack = deque([s[0]])
    
    i = 1
    while i < len(s):
        if len(stack) == 0:
            stack.append(s[i])
        elif isPair(stack[-1], s[i]):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
        
    if len(stack) > 0:
        return False
    
    return True

def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return answer
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            answer += 1
    return answer
'''

'''
<풀이 방법>
  - 재귀함수를 이용해 푼다.
  - s의 첫글자가 시작 괄호라면, 끝 괄호를 s의 뒤에서부터 찾는다.
'''
'''
rule = '()[]{}'

def check(s):
    if len(s) == 0:
        return True
    
    start = rule.find(s[0])
    if start % 2 != 0:
        return False
    
    pairI = s[::-1].find(rule[start+1])
    if pairI == -1:
        return False
    pairI = (len(s)-1) - pairI
    
    return check(s[1:pairI]) and check(s[pairI+1:])
            
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            answer += 1
    return answer
'''