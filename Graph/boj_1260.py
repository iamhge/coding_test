# DFS와 BFS
'''
※계속 쓰이는 개념! 꼭 기억할 것※

<참고>
  [파이썬 기초] 스택과 큐의 기능을 한번에 DEQUE
   : https://dongdongfather.tistory.com/72
  [Daily PS] 파이썬으로 구현하는 BFS와 DFS
   : https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
'''
import sys
from collections import deque

def DFS(graph: dict, root: int) -> list:
    visited = []
    stack = deque([root])
    
    while stack:
        n = stack.pop() # 오른쪽 끝의 항목 pop
        if n not in visited:
            visited.append(n)
            tmp = list(set(graph[n]) - set(visited))
            # 방문할 수 있는 노드가 여러개인 경우 번호가 작은 것을 먼저 방문
            # stack은 LIFO이므로 reverse해서 넣는다.
            tmp.sort(reverse=True) 
            stack += tmp # 오른쪽 끝에 항목 추가
    return visited

def BFS(graph: dict, root: int) -> list:
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft() # 왼쪽 끝의 항목 pop
        if n not in visited:
            visited.append(n)
            tmp = list(set(graph[n]) - set(visited))
            # 방문할 수 있는 노드가 여러개인 경우 번호가 작은 것을 먼저 방문
            tmp.sort()
            # 방문한 노드를 제외하고 n노드와 연결되어있는 노드들을 queue에 추가
            queue += tmp # 오른쪽 끝에 항목 추가
    return visited

N, M, V = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N+1)}

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in DFS(graph, V):
    print(i, end=" ")
print()
for i in BFS(graph, V):
    print(i, end=" ") 