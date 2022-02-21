# 섬 연결하기
'''
<풀이 방법>
  - 크루스칼 알고리즘
    - Union-find(유니온 파인드) 알고리즘
<참고>
  - 알고리즘 - 크루스칼 알고리즘(Kruskal Algorithm), 최소 신장 트리(MST)
    : https://chanhuiseok.github.io/posts/algo-33/
'''
def findRoot(parent, me):
    while parent[me] != me:
        me = parent[me]
    return me

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    
    for cost in costs:
        start, end = cost[0], cost[1]
        
        # Union-find
        stRoot = findRoot(parent, start)
        edRoot = findRoot(parent, end)
        if stRoot != edRoot:
            parent[stRoot] = edRoot
            answer += cost[2]
        
    return answer

'''
<풀이 방법>
  - costs를 비용이 적은 순으로 정렬한 후, 각 노드가 연결되어있지 않는 경우에 cost를 추가한다.
'''
from collections import deque

def canGo(start, target, n, graph):
    visited = [False for _ in range(n)]
    stack = deque([start])
    
    while stack:
        now = stack.pop()
        if now == target:
            return True
        if visited[now]:
            continue
        for node in graph[now]:
            stack.append(node)
        visited[now] = True
    
    return False

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    graph = {i: [] for i in range(n)}
    
    for cost in costs:
        if canGo(cost[0], cost[1], n, graph):
            continue
        answer += cost[2]
        graph[cost[0]].append(cost[1])
        graph[cost[1]].append(cost[0])
    
    return answer

'''
<풀이 방법>
'''