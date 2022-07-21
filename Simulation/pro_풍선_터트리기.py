# 풍선 터트리기
'''
- 아이디어는 알았으나 시간초과로 애먹음. 결국 다른 사람 해설 참고.
  참고 해설 : https://school.programmers.co.kr/questions/13657
<아이디어>
  - i번째 풍선 말고 나머지 중에서 양쪽으로 가장 작은 것을 남긴다.
    만약 왼쪽, 오른쪽에서 제일 작은 값들이 모두 i번째 풍선보다 크면 i번째 풍선은 끝까지 남지못한다.
  - 이 때, i번째 풍선이 0번째 혹은 맨 마지막 거면 무조건 남을 수 있다.
  - leftRight[i][0] = i번째 수의 왼쪽에서 가장 작은 값
    leftRight[i][1] = i번째 수의 오른쪽에서 가장 작은 값
'''
from collections import defaultdict
def solution(a):
    if len(a) < 3:
        return len(a)
    
    answer = 2
    leftRight = defaultdict(list)
    
    # 우 -> 좌
    leftMin = a[0]
    for i in range(1, len(a)-1):
        if a[i-1] < leftMin:
            leftMin = a[i-1]
        leftRight[a[i]].append(leftMin)
        
    # 좌 -> 우
    rightMin = a[-1]
    for i in range(len(a)-2, 0, -1):
        if a[i+1] < rightMin:
            rightMin = a[i+1]
        leftRight[a[i]].append(rightMin)
    
    # 비교
    for ai, lr in leftRight.items():
        if lr[0] > ai or lr[1] > ai:
            answer += 1
    
    return answer

# 더 시간 초과 3
'''
<아이디어>
  - order = (가장 작은 수 부터 a내의 순서 배열)
    order[i] 에서, a[:i]는 a[order[i]] 보다 다 작다.
    만약 order[:i] 중 order[i]보다 작은 값과 큰 값이 모두 있다면 해당 수는 마지막까지 못남는다.
'''
'''
def solution(a):
    if len(a) < 3:
        return len(a)
    
    order = []
    sortedA = sorted(a)
    answer = 0
    
    for sa in sortedA:
        order.append(a.index(sa))
    
    minIdx = maxIdx = order[0]
    
    for idx, o in enumerate(order):
        if o < minIdx:
            minIdx = o
        if o > maxIdx:
            maxIdx = o
            
        if minIdx < o and maxIdx > o:
            continue
        answer += 1
        
    return answer 
'''

# 시간 초과 2
'''
def solution(a):
    if len(a) < 3:
        return len(a)
    
    answer = 2
    
    leftMin = a[0]
    rightMin = min(a[2:])
    
    for i in range(1, len(a)-1):
        if a[i-1] < leftMin:
            leftMin = a[i-1]
        
        if a[i] == rightMin:
            rightMin = min(a[i+1:])
        
        if a[i] > leftMin and a[i] > rightMin:
            continue
        answer += 1
        
    return answer
'''

# 시간 초과 1
'''
def solution(a):
    if len(a) < 3:
        return len(a)
    
    answer = 2
    
    for i in range(1, len(a)-1):
        leftMin = min(a[:i])
        rightMin = min(a[i+1:])
        if a[i] > leftMin and a[i] > rightMin:
            continue
        answer += 1
        
    return answer
'''