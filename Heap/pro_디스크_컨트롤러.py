# 디스크 컨트롤러
import heapq

def solution(jobs):
    answer = 0
    time = 0
    heap = [] # 최소 힙 생성
    i = 0
    jobs.sort(key=lambda x: x[0]) # jobs를 작업이 요청되는 시점 순으로 정렬
    
    while True:
        # 작업하지 않고 비는 시간을 보정한다.
        # ex) 현재 시점에 할 작업이 없지만 아직 남은 job이 있는 경우
        if i < len(jobs) and len(heap) == 0:
            time = max(time, jobs[i][0])
            
        # 현재 시점에서 수행할 수 있는 작업을 모두 최소 heap에 넣는다.
        while i < len(jobs):
            if jobs[i][0] <= time:
                # 작업의 소요시간이 작은 순으로 heap에 push 한다.
                heapq.heappush(heap, (jobs[i][1], jobs[i])) # (작업 소요시간, jobs[i])
                i += 1
            else:
                break
        
        if len(heap) <= 0: break
        
        job = heapq.heappop(heap)
        time += job[0]
        answer += time - job[1][0]
        
    return answer // len(jobs)