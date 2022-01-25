# 거리두기 확인하기
# 거리두기 확인하기
'''
<풀이 방법>
  - BFS
    - 현재 좌표의 상, 하, 좌, 우 를 검사한다. 
    - 상, 하, 좌, 우의 P로부터의 맨해튼거리는 현재 좌표의 P로부터의 맨해튼 거리 + 1 이다.
    - 'X'가 나오면 벽과 같이 간주하여 큐에 넣지 않는다.
'''
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(place, visited, start):
    queue = deque([start])
    
    while queue:
        x, y, m = queue.popleft() # m = P로 부터의 맨해튼거리
        visited[y][x] = True
            
        if place[y][x] == 'P':
            m = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                if place[ny][nx] == 'P':
                    if m < 2:
                        return 0, visited
                elif place[ny][nx] == 'X':
                    continue
                queue.append((nx, ny, m+1))
                
    return 1, visited

def check(place):
    visited = [[False for _ in range(5)] for _ in range(5)]
    for x in range(5):
        for y in range(5):
            if not visited[y][x] and place[y][x] == 'P':
                result, visited = BFS(place, visited, (x, y, 0))
                if result == 0:
                    return 0
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check(place))
        
    return answer