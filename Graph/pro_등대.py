'''
다른 사람 풀이 봄
<조건 해석>
1) 노드의 개수는 n, vertex의 개수가 n-1이며, 모든 길이 연결되어있으므로 Tree 구조이다.
2) Tree 구조의 특성을 이용하도록 한다.
<풀이 방법>
1) leaf node는 불을 키지 않는다.
2) 자식 노드 중 하나라도 불을 껐을 경우, 부모 노드는 불을 킨다.
3) 자식 노드 모두 불을 켰을 경우, 부모 노드는 불을 꺼도 끈다.
<오답 노트>
- 틀린 풀이는 아니었으나, 시간 초과가 발생하였다.
  이전 풀이는 부모 노드가 불을 켰는지 여부에 따라 자식 노드에 불을 킬지, 끌지가 정해졌다.
  그래서 자식 노드에 불을 킬 수도, 끌 수도 있었다.
  그러나 정답 풀이는 자식 노드에 따라 정해진다.
  따라서 리프 노드부터 차례로 up하면 킬지 말지 여부가 정확히 정해진다.
  so, 시간 초과가 났었던 것.
<참고 풀이>
[프로그래머스] 등대
: https://velog.io/@ddongh1122/프로그래머스-등대
'''
# 재귀 깊이 때문에 런타임 에러 발생.. 아래 두 줄 추가로 런타임 문제 해결
import sys
sys.setrecursionlimit(10**6)

from collections import deque, defaultdict

# 1: 불 키지 않는다.
# 0: 불 킨다.
def turn(node, onOff, tree, light):
    # leafNode인 경우 불을 키지 않는다.
    if node not in tree:
        return 1 # 불 키지 않음
    
    childrenLight = 0
    
    for child in tree[node]:
        childrenLight += turn(child, onOff, tree, light)
    
    # 자식 노드들이 모두 불 켰을 경우 (부모 노드가 키지 않아도 된다.)
    if childrenLight == 0:
        return 1
    # 자식 노드들 중 하나라도 불 껐을 경우 (부모 노드가 불 켜야 된다.)
    light[node] = 0
    return 0

def makeTree(n, vertex, root):
    stack = deque([root])
    tree = defaultdict(list)
    visited = [False]*(n+1)
    visited[root] = True
    
    while stack:
        node = stack.pop()
        
        for neigh in vertex[node]:
            if visited[neigh]:
                continue
            tree[node].append(neigh)
            stack.append(neigh)
            visited[neigh] = True
            
    return tree

def solution(n, lighthouse):
    vertex = [[] for _ in range(n+1)]

    for lh in lighthouse:
        vertex[lh[0]].append(lh[1])
        vertex[lh[1]].append(lh[0])
        
    tree = makeTree(n, vertex, 1)
    
    start = 1
    light = [1] * (n+1)
    turn(start, 1, tree, light)
    
    return light.count(0)

# 시간 초과 나는 풀이
'''
<풀이 방법>
1) 이전 노드(부모 노드)에 불을 켰을 경우 -> 현재 노드에 불을 키거나 끌 수 있다.
2) 부모 노드에 불을 껐을 경우 -> 현재 노드에 무조건 불을 켜야한다.
3) 현재 노드에 불을 킬 경우와 끌 경우 중 더 최소로 킬 수 있는 경우를 return 한다.
'''
'''
import sys
sys.setrecursionlimit(10**6)

# onOff: 이전 노드에 불을 붙였는지의 여부, 1: on, 0: off
# return 값: 현재 노드부터 하위 노드들의 불을 최소로 킬 수 있는 경우의 불 개수
def turn(node, onOff, vertex, visited):
    onResult = 1 # 현재 노드에 불을 킬 경우
    offResult = 0 # 현재 노드에 불을 끌 경우
    
    for neighbor in vertex[node]:
        if visited[neighbor]:
            continue
            
        visited[neighbor] = True
        # node 불 킨다.
        onResult += turn(neighbor, 1, vertex, visited)
        # node 불 끈다. (이전 노드에서 불 켰던 경우만)
        if onOff == 1:
            offResult += turn(neighbor, 0, vertex, visited)
        visited[neighbor] = False
        
    if onOff == 1:
        onResult = min(onResult, offResult)
    
    return onResult

def solution(n, lighthouse):
    vertex = [[] for _ in range(n+1)]

    for lh in lighthouse:
        vertex[lh[0]].append(lh[1])
        vertex[lh[1]].append(lh[0])
    
    visited = [False] * (n+1)
    start = 1
    visited[start] = True
    
    return turn(start, 1, vertex, visited)
'''