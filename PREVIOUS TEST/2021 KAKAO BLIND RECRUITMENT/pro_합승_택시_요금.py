# 합승 택시 요금
'''
<풀이 방법>
  Floyd-Warshall (플로이드 워셜) 알고리즘
'''
INF = 100001*200*3

def FloydWarshall(n, dist, nodes):
    for now in range(1, n+1):
        for peer1 in range(1, n+1):
            for peer2 in range(1, n+1):
                if dist[peer1][now] + dist[now][peer2] < dist[peer1][peer2]:
                    dist[peer1][peer2] = dist[peer1][now] + dist[now][peer2]
                    dist[peer2][peer1] = dist[peer1][now] + dist[now][peer2]
    return dist

def solution(n, s, a, b, fares):
    answer = INF
    nodes = {i: [] for i in range(1, n+1)}
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for fare in fares: 
        nodes[fare[0]].append(fare[1])
        nodes[fare[1]].append(fare[0])
        dist[fare[0]][fare[1]] = fare[2]
        dist[fare[1]][fare[0]] = fare[2]
    
    dist = FloydWarshall(n, dist, nodes)
    
    for i in range(1, n+1):
        answer = min(dist[s][i] + dist[i][a] + dist[i][b], answer)
    
    return answer

# 통과 코드
'''
<풀이 방법>
  - 다익스트라 최소 경로 알고리즘 사용
    1) s, a, b 각각에서 다른 모든 노드까지 최소 경로를 구한다.
    2) s-> 환승지 + 환승지 -> a + 환승지 -> b가 최소인 환승지를 구한다.
'''
'''
import heapq

INF = 100001*200*3

def Dijkstra(n, start, nodes):
    dist = [INF] * (n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cost, now = heapq.heappop(queue)
        if cost > dist[now]:
            continue
        for peer in nodes[now]:
            totalCost = peer[0] + cost
            if totalCost < dist[peer[1]]:
                dist[peer[1]] = totalCost
                heapq.heappush(queue, (totalCost, peer[1]))

    return dist

def solution(n, s, a, b, fares):
    answer = INF
    nodes = {i: [] for i in range(1, n+1)}
    for fare in fares: 
        nodes[fare[0]].append((fare[2], fare[1]))
        nodes[fare[1]].append((fare[2], fare[0]))
    
    sp = Dijkstra(n, s, nodes)
    ap = Dijkstra(n, a, nodes)
    bp = Dijkstra(n, b, nodes)
    
    for i in range(1, n+1):
        answer = min(answer, sp[i] + ap[i] + bp[i])
    
    return answer
'''
# 틀린 코드
'''
<틀린 이유>
  - 다익스트라 알고리즘을 사용한 줄 알았는데 매번 가장 거리가 짧은 노드를 선택해서 임의의 횟수의 과정을 계속적으로 반복해야한다는 조건을 만족하지 못한다.
  - 정확성 테스트 4 통과 못함.
  - 효율성 테스트 대부분 통과 못함.
'''
'''
from collections import deque

INF = 100001*200*3

def Dijkstra(n, start, nodes):
    visited = [False] * (n+1)
    p = [INF] * (n+1)
    p[start] = 0
    queue = deque([start])
    
    while queue:
        now = queue.popleft()
    
        if visited[now]: continue
        
        visited[now] = True
        for peer in nodes[now]:
            p[peer[0]] = min(p[peer[0]], p[now] + peer[1])
            queue.append(peer[0])

    return p

def solution(n, s, a, b, fares):
    answer = INF
    nodes = {i: [] for i in range(1, n+1)}
    for fare in fares:
        nodes[fare[0]].append((fare[1], fare[2]))
        nodes[fare[1]].append((fare[0], fare[2]))
    
    sp = Dijkstra(n, s, nodes)
    ap = Dijkstra(n, a, nodes)
    bp = Dijkstra(n, b, nodes)
    
    for i in range(1, n+1):
        answer = min(answer, sp[i] + ap[i] + bp[i])
    
    return answer
'''