# 짝지어 제거하기
'''
<풀이 방법>
  - 짝을 이룰 수 없다면 stack에 넣고,
    짝을 이룰 수 있다면 stack에서 뺀다.
  - s의 모든 글자를 순회했는데, stack에 글자가 남아있다면 0
  - s의 모든 글자를 순회하지 않았는데 stack이 빈다면 다시 stack에 추가한다.
'''
from collections import deque

def solution(s):
    stack = deque([s[0]])
    
    if len(s) % 2 != 0: return 0
    
    i = 1
    while i < len(s):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    
    if len(stack) > 0:
        return 0
    
    return 1

# 시간 초과
'''
<풀이 방법>
  - 짝지어 제거하면 다시 처음으로 돌아가서 짝을 제거한다.
'''
'''
def solution(s):
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            s = s[:i-1] + s[i+1:]
            i = 0
        i += 1

    if len(s) == 0:
        return 1

    return 0
'''

# 틀린 코드
'''
<풀이 방법>
  - 데칼코마니를 이루어야 한다.
  - 같은 알파벳이 2개 붙어있기 전까지의 문자가 decalcomanie,
    연속적으로 짝이 있는 구간(combo 구간)의 길이가 l,
    짝이 없어지는 인덱스가 j라면
    -> decalcomanie[::-1] == s[j:j+l] 여야한다.
<오답 노트>
  - 데칼코마니를 이루지 않고도 성공적으로 수행될 수 있다.
  반례 ex) "abccaeeaba" -> 1
'''
'''
def solution(s):
    combo = False
    decalcomanie = ""
    
    i = 0
    while i < len(s)-1:
        if s[i] != s[i+1]:
            if combo == False:
                decalcomanie += s[i]
            else:
                if decalcomanie[::-1] != s[i:i+len(decalcomanie)]:
                    return 0
                combo = False
                i += len(decalcomanie)-1
                decalcomanie = ""
        else:
            if combo == False: # combo 시작
                combo = True
            i += 1 # i, i+1을 검사했으므로 다음에 i+2 구간을 검사하도록 한다.
        i += 1
        
    if decalcomanie != s[i:]:
        return 0
    
    return 1
'''