# 무인도 여행
'''
<풀이 방법>
- BFS
'''
from collections import deque 

# 상 하 좌 우
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열

def island(maps, start, visited):
    queue = deque([])
    queue.append(start)
    day = int(maps[start[0]][start[1]])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])) and (not visited[nx][ny]) and (maps[nx][ny] != "X") :
                queue.append((nx, ny))
                visited[nx][ny] = True
                day += int(maps[nx][ny])

    return day

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != "X":
                answer.append(island(maps, (i, j), visited))
                
    if len(answer) == 0:
        return [-1]
    return sorted(answer)