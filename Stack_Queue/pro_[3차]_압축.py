# [3차] 압축
from collections import deque

def solution(msg):
    answer = []
    dictionary = [" "]
    dictionary.extend(list(chr(ord('A') + i) for i in range(26)))
    queue = deque(list(msg))

    w = ""
    while queue:
        w += queue.popleft()
        if len(queue) == 0:
            break
        if w + queue[0] not in dictionary:
            dictionary.append(w + queue[0]) 
            answer.append(dictionary.index(w))
            w = ""

    answer.append(dictionary.index(w))
    
    return answer