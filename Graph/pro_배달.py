# 배달
'''
<풀이 방법>
  - 1에서부터 모든 node까지의 최단 경로를 구한다.
    1) queue에 root(현재 문제는 1로 고정)를 넣는다.
    2) queue에서 현재 node를 꺼낸 후, 현재 node와 이어진 vertex를 검사한다.
    3) edge의 가중치 + 현재 node까지의 경로가 vetex의 경로보다 적으면 업데이트후, vertex를 queue에 넣는다.
    4) 2~3) 반복한다.
  - makeGraph : 문제 풀이에 편리하도록 dict타입의 양방향 그래프를 나타내는 형태로 변경한다.
    ex) road = [[1, 2, 1], [2, 3, 3] -> graph = 1: {(2, 1)}, 2: {(1, 1), (3, 3)}, 3: {(2, 3)}}
  - shortest : root에서부터 모든 node까지의 최단 경로를 검사하여 배열로 반환한다.
'''
from collections import deque

INF = 500001

def makeGraph(N, road):
    graph = {i: set() for i in range(1, N+1)}
    for v in road:
        graph[v[0]].add((v[1], v[2]))
        graph[v[1]].add((v[0], v[2]))
    return graph

def shortest(N, root, graph):
    queue = deque([root])
    p = [INF for _ in range(N+1)]
    p[root] = 0
    
    while queue:
        now = queue.popleft()
        
        for edge in graph[now]:
            if p[edge[0]] > p[now] + edge[1]:
                p[edge[0]] = p[now] + edge[1]
                queue.append(edge[0])
        
    return p
    
def solution(N, road, K):
    answer = 0
    graph = makeGraph(N, road)
    for k in shortest(N, 1, graph):
        if k <= K:
            answer += 1
    return answer