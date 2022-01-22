# 빛의 경로 사이클
'''
<주의할 점>
  - 이미 방문한 '좌표+방향'인 경우, 사이클에 속해있다는 것을 의미하므로 사이클이 발생하지 않는 '시작좌표+방향'이라고 할 수 있다.
'''
# 하 좌 상 우
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 직진 -> 그대로, 좌회전 -> i -= 1, 우회전 -> i += 1
direction = {'S': 0, 'L': -1, 'R': 1}

def validRange2(M, N, nx, ny):
    if nx < 0:
        nx += M
    elif nx >= M:
        nx -= M
    if ny < 0:
        ny += N
    elif ny >= N:
        ny -= N
    return nx, ny

def validRange1(L, nx):
    if nx < 0:
        nx += L
    elif nx >= L:
        nx -= L
    return nx

# grid, 방문기록, 행의 길이, 열의 길이, 시작점의 x 좌표, 시작점의 y 좌표, 시작 방향의 index (ex. 0인 경우 dx[0], dy[0])
def isCycle(grid, visited, M, N, m, n, d): 
    cycleLen = 0
    nx, ny = m, n
    nd = d
    
    # 하 좌 상 우
    while not visited[ny][nx][nd]:
        visited[ny][nx][nd] = True # in을 표시
        
        nd = validRange1(4, nd + direction[grid[ny][nx]]) # 바뀌는 방향
        nx, ny = validRange2(M, N, nx + dx[nd], ny + dy[nd]) # 이동될 위치
        
        cycleLen += 1
    
    if nx == m and ny == n and nd == d:
        return cycleLen, visited
    return 0, visited
    

def solution(grid):
    answer = []
    N = len(grid)
    M = len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
    
    for n in range(N):
        for m in range(M):
            for d in range(4):
                cycleLen, visited = isCycle(grid, visited, M, N, m, n, d)
                if cycleLen > 0:
                    answer.append(cycleLen)
    
    return sorted(answer)