# 프린터
'''
<풀이 방법>
  queue : 인쇄 대기목록
  - priorities의 최댓값보다 queue에서 popleft한 문서의 priority가 작으면 대기줄 뒤에 삽입
  - popleft한 문서의 priority가 최댓값이면
      1) priorities에서 해당 priority값을 -1로 변경해 이미 출력된 문서임을 표시
      2) location에 해당하는 문서일 경우 sequence 값을 바로 리턴
'''
from collections import deque

def solution(priorities, location):
    queue = deque([(i, priorities[i]) for i in range(len(priorities))])
    seq = 0
    
    while queue:
        nowLoc, nowPriority = queue.popleft()
        if max(priorities) > nowPriority:
            queue.append((nowLoc, nowPriority))
        else:
            seq += 1
            priorities[nowLoc] = -1
            if nowLoc == location:
                break
        
    return seq