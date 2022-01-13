# 전력망을 둘로 나누기
'''
<풀이 방법>
  - wires를 그래프의 edge로 생각한다.
  - makeGraph : wires를 문제 풀이에 편리하도록 dict타입의 양방향 그래프를 나타내는 형태로 변경한다.
    ex) wires = [[1, 2], [1, 3]] -> graph = {1: {2, 3}, 2: {1}, 3: {1}}
  - countConnected : root에서부터 연결되어있는 노드의 수를 구한다.
  1) wires의 각 wire를 제외한 후, 하나의 전력망에 연결되어있는 송전탑의 수(= c)를 구한다.
  2) 두 전령망이 가지고 있는 송전탑 개수의 차이 = |2*c - n|
  3) 각 wire를 제거한 상황을 모두 검사한다. -> 완전탐색
'''
from collections import deque

def countConnected(n, root, graph):
    cnt = 0
    visited = [False for i in range(n+1)]
    stack = deque([root])
    
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        cnt += 1
        visited[node] = True
        for vertex in graph[node]:
            stack.append(vertex)
    return cnt

def makeGraph(n, wires):
    graph = {i: set() for i in range(1, n+1)}
    for wire in wires:
        graph[wire[0]].add(wire[1])
        graph[wire[1]].add(wire[0])
    return graph

def solution(n, wires):
    answer = n
    
    graph = makeGraph(n, wires)
    
    for wire in wires:
        # graph에서 현재 wire에 대한 edge를 제거한다.
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        
        c = countConnected(n, wire[0], graph)
        if 2*c - n > 0:
            answer = min(answer, 2*c - n)
        else:
            answer = min(answer, n - 2*c)
        
        # 제거했던 edge를 다시 graph에 추가한다.
        graph[wire[0]].add(wire[1])
        graph[wire[1]].add(wire[0])
    
    return answer