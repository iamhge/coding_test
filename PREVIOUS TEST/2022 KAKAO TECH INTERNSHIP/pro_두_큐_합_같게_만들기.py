# 두 큐 합 같게 만들기
'''
<풀이 방법>
  - 그저 Greedy 구현...
<오답 노트>
  - 이전에 틀렸던 이유는 sum 함수를 계속 반복적으로 사용했기 때문. 다음부터 조심하자.
'''
from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    target = (sum(queue1) + sum(queue2)) // 2
    maxTry = len(queue1) * 3
    
    sumQ1 = sum(queue1)
    
    while sumQ1 != target:
        if answer >= maxTry:
            return -1
        if sumQ1 < target:
            popNum = queue2.popleft()
            sumQ1 += popNum
            queue1.append(popNum)
        else:
            popNum = queue1.popleft()
            sumQ1 -= popNum
            queue2.append(popNum)
        
        answer += 1
    
    return answer
'''
from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    target = (sum(queue1) + sum(queue2)) // 2
    maxTry = len(queue1) * 2
    
    sumQ1 = sum(queue1)
    
    while sumQ1 != target:
        if answer > maxTry:
            return -1
        if sumQ1 < target:
            new = queue2.popleft()
            sumQ1 += new
            queue1.append(new)
        else:
            new = queue1.popleft()
            sumQ1 -= new
            queue2.append(new)
        answer += 1
    
    return answer
'''
# 시간 초과 + 틀린 풀이 대 환장 조합
'''
<풀이 방법>
  - 어차피 순서는 계속 일정하다. queue1과 queue2는 원형큐와 같이 이어져있는데, 
    그 중에서 만들어 지는가 아닌가 + 어떻게 만들어지는가를 판단해야한다.
'''
'''
def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    target = (sum(queue1) + sum(queue2)) // 2
    maxTry = len(queue1)
    answer1 = 0
    answer2 = 0
    
    roundQueue = queue1 + queue2 + queue1
    i = 0
    j = 4
    while i < maxTry*2:
        if sum(roundQueue[i:j]) == target:
            break
        elif sum(roundQueue[i:j]) < target:
            j += 1
        else:
            i += 1
        answer1 += 1
        

    roundQueue = queue2 + queue1 + queue2
    i = 0
    j = 4
    while i < maxTry*2:
        if sum(roundQueue[i:j]) == target:
            break
        elif sum(roundQueue[i:j]) < target:
            j += 1
        else:
            i += 1
        answer2 += 1
    
    # roundQueue = queue2 + queue1 + queue2
    # for i in range(maxTry):
    #     for j in range(maxTry):
    #         if sum(roundQueue[i:i+j+1]) == target:
    #             answer2 = i + (i+j+1) - maxTry
    #             break
    #     if answer2 < maxTry*2 : break
        
    print(answer1, answer2)
    return min(answer1, answer2) if (answer1 < maxTry*2) or (answer2 < maxTry*2) else -1


'''

# 시간 초과
'''
<풀이 방법>
  - greedy
'''
'''
from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    target = (sum(queue1) + sum(queue2)) // 2
    maxTry = len(queue1) * 2
    
    while sum(queue1) != target:
        if answer > maxTry:
            return -1
        if sum(queue1) < target:
            queue1.append(queue2.popleft())
        else:
            queue2.append(queue1.popleft())
        answer += 1
    
    return answer
'''