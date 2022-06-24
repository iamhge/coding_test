# 단어 변환
'''
<풀이 방법>
  1) if 한글자만 변경이 가능하면 -> queue에 넣는다.
  2) if target이면 -> result 업데이트.
'''
from collections import deque

def isDifferentOneChar(a, b):
    diff = 0

    for i in range(0, len(a)):
        if a[i] == b[i]: continue
        diff += 1
    if diff == 1: return True

    return False

def solution(begin, target, words):
    answer = len(words) + 1
    queue = deque([(begin, 0, {word: False for word in words})])
    
    while queue:
        now, num, visited = queue.popleft()
        
        if now == target:
            answer = min(num, answer)
            continue
        for word in words:
            if isDifferentOneChar(word, now) and not visited[word]:
                visited[word] = True
                queue.append((word, num + 1, visited))
    
    if answer > len(words): return 0
    return answer

# 다른 사람 풀이
'''
<아이디어>
  1) yeild 사용
    - generator를 반환한다. return을 여러번 하는 것이라고 생각하면 됨.
    참고 : https://www.daleseo.com/python-yield/
  2) zip 사용
    - zip(a, b)를 하면 a의 요소와 b의 요소가 짝지어져서 return 된다.
    참고 : https://www.daleseo.com/python-zip/
<풀이 방법>
  1) get_adjacent(current, words)
     current에서 한 글자 다른 단어들을 반환한다.
  2) dist
     dist
'''
'''
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
'''