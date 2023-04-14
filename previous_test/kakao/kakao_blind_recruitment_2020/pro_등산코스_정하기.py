# 등산코스 정하기
'''
다른 사람 풀이 참고
<풀이 방법>
- 다익스트라
- point 1. gate를 모두 heap에 넣고 시작한다.
  이렇게 하면 gate들 중 어디든에서 각 노드들까지 최소 intensity가 나오는 경로를 찾을 수 있다.
- point 2. 출입구는 나가는 간선만 존재하고, 산봉우리는 들어오는 간선만 존재한다.
  -> 이를 통해 출입구는 한번만 통과, 산봉우리 도착 시 종료 라는 조건을 충족할 수 있다.
  => 근데 이거 하면 시간 초과 나는 이유좀 ... => in list 연산이 많을 때는 list 대신 set을 쓰자...
<참고>
등산코스 정하기
: https://velog.io/@dasd412/%EB%93%B1%EC%82%B0%EC%BD%94%EC%8A%A4-%EC%A0%95%ED%95%98%EA%B8%B0
'''

from collections import defaultdict
import heapq

INF = 10000001

def dijkstra(n, summits, gates, vertex):
    intensity = [INF]*(n+1)
    queue = []
    
    # 여기가 시간을 줄이는 핵심.
    # gate를 모두 heap에 넣는다.
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(queue, (0, gate))
    
    while queue:
        w, node = heapq.heappop(queue)
        
        if intensity[node] < w:
            continue
        
        for neigh, nw in vertex[node]:
            newIntensity = max(intensity[node], nw)
            if newIntensity < intensity[neigh]:
                intensity[neigh] = newIntensity
                if neigh not in summits:
                    heapq.heappush(queue, (intensity[neigh], neigh))
    
    # answer
    answer = [0, INF]
    for summit in sorted(summits):
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
            
    return answer
    
def solution(n, paths, gates, summits):
    vertex = defaultdict(list)
    for path in paths:
        # if path[0] in gates or path[1] in summits:
        #     vertex[path[0]].append([path[1], path[2]])
        # if path[1] in gates or path[0] in summits:
        #     vertex[path[1]].append([path[0], path[2]])
        
        vertex[path[0]].append([path[1], path[2]])
        vertex[path[1]].append([path[0], path[2]])
        
    # 이거 하나 set으로 바꿨다구... 통과되구... 나 정말 속상해...
    return dijkstra(n, set(summits), set(gates), vertex)

# 시간 초과
'''
<풀이 방법>
- 다익스트라
'''
'''
from collections import defaultdict
import heapq

INF = 10000001

def dijkstra(n, start, end, summits, gates, vertex):
    intensity = [INF]*(n+1)
    intensity[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        w, node = heapq.heappop(queue)
        
        if intensity[node] < w:
            continue
        
        for neigh, nw in vertex[node]:
            if (neigh != start and neigh in gates) or (neigh != end and neigh in summits):
                continue
            
            if max(intensity[node], nw) < intensity[neigh]:
                intensity[neigh] = max(intensity[node], nw)
                heapq.heappush(queue, (intensity[neigh], neigh))
    
    return intensity[end]
    

def solution(n, paths, gates, summits):
    answer = [0, INF]
    vertex = defaultdict(list)
    
    for path in paths:
        vertex[path[0]].append([path[1], path[2]])
        vertex[path[1]].append([path[0], path[2]])
        
    for gate in gates:
        for summit in summits:
            nowInten = dijkstra(n, gate, summit, summits, gates, vertex)
            if nowInten < answer[1]:
                answer = [summit, nowInten]
    
    return answer
'''

# 시간 초과
'''
<풀이 방법>
- 플로이드 워셜
'''
'''
from collections import defaultdict

INF = 10000001

def solution(n, paths, gates, summits):
    answer = [0, INF]
    intensity = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        intensity[i][i] = 0
    
    for path in paths:
        intensity[path[0]][path[1]] = path[2]
        intensity[path[1]][path[0]] = path[2]
        
    gatesRest = set(i+1 for i in range(n))- set(summits)
    summitsRest = set(i+1 for i in range(n))- set(gates)
    rests = summitsRest - set(summits)
    
    for summit in summitsRest:
        for gate in gatesRest:
            for rest in rests:
                intensity[gate][summit] = min(intensity[gate][summit], max(intensity[gate][rest], intensity[rest][summit]))
    
    summits.sort()
    for summit in summits:
        for gate in gates:
            if intensity[gate][summit] < answer[1]:
                answer = [summit, intensity[gate][summit]]
    
    return answer
'''