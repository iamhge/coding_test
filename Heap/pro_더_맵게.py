# 더 맵게
'''
<참고>
  [파이썬] heapq 모듈 사용법
   : https://www.daleseo.com/python-heapq/
'''
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return count
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        mix = a + b*2
        heapq.heappush(scoville, mix)
        count += 1
    
    if scoville[0] >= K:
        return count
    
    return -1