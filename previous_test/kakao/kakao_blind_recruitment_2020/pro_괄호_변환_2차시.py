# 괄호 변환 2차시
from collections import deque

def disuniteBracket(bracket):
    op = cl = 0
    for i in range(len(bracket)):
        if bracket[i] == '(':
            op += 1
        else:
            cl += 1
        if op == cl:
            u = bracket[:i+1]
            v = bracket[i+1:]
            break
    return u, v

def isCollectString(bracket):
    if bracket[0] == ')': return False
    queue = deque(['('])
    i = 1
    while queue:
        if i >= len(bracket):
            return False
        if bracket[i] == '(':
            queue.append('(')
        else:
            queue.popleft()
        i += 1
    if i < len(bracket):
        return False
    return True

def changeDirectionOfBracket(bracket):
    result = ''
    for w in bracket:
        if w == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    answer = ''
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == '': return p

    if isCollectString(p):
        # print(p, "는 올바른 괄호 문자열이다.")
        return p
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = disuniteBracket(p)
    # print("u :", u, ", v :", v)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if isCollectString(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        answer = u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer += '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += solution(v)
        # 4-3. ')'를 다시 붙입니다.
        answer += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        answer += changeDirectionOfBracket(u[1:-1])
            
    return answer