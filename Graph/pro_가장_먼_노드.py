# 가장 먼 노드
'''
<풀이 방법>
  BFS
  - 인접한 노드에 방문하지 않았다면 queue에 넣고 distance를 업데이트한다.
'''
from collections import deque

def BFS(n, start, vertex, dist):
    queue = deque([start])
    visited = [False] * (n+1)
    
    while queue:
        node = queue.popleft()
        
        for nextNode in vertex[node]:
            if not visited[nextNode]:
                dist[nextNode] = min(dist[nextNode], dist[node] + 1)
                queue.append(nextNode)
                visited[nextNode] = True
                
    return dist

def solution(n, edge):
    vertex = {i: [] for i in range(1, n+1)}
    for e in edge:
        vertex[e[0]].append(e[1])
        vertex[e[1]].append(e[0])
        
    dist = [n] * (n+1)
    dist[1] = 0
    
    dist = BFS(n, 1, vertex, dist)
    
    return dist.count(max(dist[1:]))