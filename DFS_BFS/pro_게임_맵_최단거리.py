# 게임 맵 최단거리
'''
<풀이 방법>
  - BFS
'''
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(root, maps, n, m, target):
    queue = deque([(root[0], root[1], 1)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == target[0] and y == target[1]:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((nx, ny, cnt + 1))
                visited[ny][nx] = True
    
    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return BFS((0, 0), maps, n, m, (m-1, n-1))

# 시간 초과
'''
<풀이 방법>
  - DFS
'''
'''
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(root, maps, n, m, target):
    stack = deque([root])
    visited = [[n*m+1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    
    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and visited[ny][nx] > visited[y][x] + 1:
                stack.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1
    
    return visited[target[1]][target[0]]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    result = DFS((0, 0), maps, n, m, (m-1, n-1)) 
    if result == n*m + 1:
        return -1
    else:
        return result
'''