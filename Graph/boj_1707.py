# 이분 그래프
'''
<아이디어>
  BFS 이용
<개념>
  이분 그래프 : 인접한 정점끼리 서로 다른 색으로 칠해서 
                모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
  (출처)https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html
<틀린 이유>
  1. 연결 그래프, 비연결 그래프 모두 고려하지 않음.
  2. 시간 초과
  3. 경계값(`for i in range(1, V+1):` 에서 V+1까지 순회해야했는데, V까지 순회)
  4. `result = answer[0]`을 for문 밖에 둬서 
     'NO' 출력 후 'YES'가 나와야하는 상황에 'NO'가 출력됨.
  5. DFS 도전했는데 틀림.
'''
import sys
from collections import deque

# BFS
def ColoringBFS(visited: list, graph: dict, start: int) -> bool:
    queue = deque([start])
    visited[start] == True

    while queue:
        n = queue.popleft()

        for near in list(graph[n]):
            if visited[near] == -1:
                visited[near] = not visited[n] # True, False로 coloring
                queue.append(near)
            elif visited[near] == visited[n]:
                return False
    return True

K = int(sys.stdin.readline().rstrip())
answer = ["YES", "NO"]

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = {i: set() for i in range(1, V+1)}
    result = answer[0]

    for _ in range(E):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].add(B)
        graph[B].add(A)

    # 연결그래프와 비연결 그래프 모두 확인해야한다.
    # so, 모든 정점에 대해 확인해야 함.
    visited = [-1]*(V+1) # visited[n] == -1 이면 방문하지 않은 노드라는 것.
    for i in range(1, V+1):
        if visited[i] == -1:
            if ColoringBFS(visited, graph, i) == False:
                result = answer[1]
                break
    print(result)