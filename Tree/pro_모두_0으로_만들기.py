# 모두 0으로 만들기
# 다른 사람 코드 참고
'''
<풀이 방법>
  - DFS
  - leaf 노드에서부터 자식 노드가 0이 되게 부모 노드에 연산을 한다.
  - DFS를 통해 root 노드 부터 leaf 까지 탐색한다.
<개념>
  - 트리 구조는 어떤 노드든 루트 노드가 될 수 있다는 성질을 가지고 있다.
<참고>
  [프로그래머스] 모두 0으로 만들기 (Python)
  : https://velog.io/@piopiop/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EB%91%90-0%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python
'''
# runtime에러 나서 아래 코드 추가 시키니 됐음.. 재귀라서 런타임 에러 났음
import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

answer = 0

def dfs(node, a, vertex, visited):
    global answer
    visited[node] = True
    
    for neighbor in vertex[node]:
        if not visited[neighbor]:
            a[node] += dfs(neighbor, a, vertex, visited)
            
    answer += abs(a[node])
    
    return a[node]
    
def solution(a, edges):
    if sum(a) != 0:
        return -1
    global answer
    
    vertex = defaultdict(list)
    for edge in edges:
        vertex[edge[0]].append(edge[1])
        vertex[edge[1]].append(edge[0])
        
    visited = [False] * len(a)
    
    dfs(0, a, vertex, visited)
    
    return answer

# 틀린 코드
'''
<풀이 방법>
  - leaf 노드에서부터 root 노드로 올라가면서, leaf 노드의 가중치를 부모노드에 더해준다.
<오답 노트>
  - leaf 노드를 간선이 1개인 노드들로 생각했는데, 그렇게 하면 안되는 것 같다.
'''
'''
from collections import defaultdict
from collections import deque

def solution(a, edges):
    answer = 0
    vertex = defaultdict(list)
    for edge in edges:
        vertex[edge[0]].append(edge[1])
        vertex[edge[1]].append(edge[0])
        
    visited = [False] * len(a)
    
    queue = deque([])
    for node in vertex:
        if len(vertex[node]) == 1:
            queue.append(node)
    
    while queue:
        node = queue.popleft()
        visited[node] = True
        
        for neighbor in vertex[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                answer += abs(a[node])
                a[neighbor] += a[node]
                a[node] = 0
                break

    if set(a) != {0}:
        answer = -1
        
    return answer
'''

# 틀린 코드
'''
from collections import defaultdict

def solution(a, edges):
    answer = 0
    vertex = defaultdict(list)
    for edge in edges:
        vertex[edge[0]].append(edge[1])
        vertex[edge[1]].append(edge[0])
        
    visited = [False] * len(a)

    for node in sorted(vertex, key = lambda x: len(vertex[x])):
        visited[node] = True
        print("node",node)
        for neighbor in vertex[node]:
            if not visited[neighbor]:
                print("neighbor:",neighbor)
                answer += abs(a[node])
                a[neighbor] += a[node]
                a[node] = 0
                break
        print(a)
    if set(a) != {0}:
        answer = -1
        
    return answer
'''