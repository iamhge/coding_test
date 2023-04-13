# 경주로 건설
'''
해설 찾아본 문제.
<풀이 방법>
- 다익스트라 + DFS
- pay는 같은데 방향은 다른 경우, 다른 결과가 나올 수 있다.
  -> 방향이 추가된 3차원 배열을 사용해야하는 이유.
<오답 노트>
1) 시간 초과
   - 다익스트라를 이용해야했으나, 하지않음.
2) 방향도 고려해야한다.
   - 방향이 다르면 pay가 같을지라도 이후 다른 결과가 나올 수 있다. 따라서 방향에 따른 pay 계산도 해줘야한다.
'''
from collections import deque

INF = 1000000000000

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(board):
    n = len(board)
    x = 0
    y = 0
    direct = -1
    
    # payment[x][y][direct] = direct 방향의 x, y위치에서 payment
    payment = [[ [INF]*4  for __ in range(n) ] for _ in range(n)]
    
    stack = deque([(x, y, direct)])
    payment[x][y] = [-500, -500, -500, -500] # (0, 0)에서는 무조건 직선 도로인데, 코너로 측정되므로 빼준다.
    
    while stack:
        x, y, d = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if i == d and payment[x][y][d] + 100 < payment[nx][ny][i]:
                    payment[nx][ny][i] = payment[x][y][d] + 100
                    stack.append((nx, ny, i))
                elif payment[x][y][d] + 600 < payment[nx][ny][i]:
                    payment[nx][ny][i] = payment[x][y][d] + 600
                    stack.append((nx, ny, i))

    return min(payment[n-1][n-1])

# 반례 있음
'''
[[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
4500
'''
'''
from collections import deque

INF = 1000000000000

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def printP(payd):
    for pd in payd:
        for p in pd:
            elif p[0] == INF:
                print("___", end=" ")
            else:
                print(p[0], end=" ")
                
        print()
    print()
def solution(board):
    n = len(board)
    x = 0
    y = 0
    direct = -1
    
    payDirect = [[[INF, -1] for __ in range(n)] for _ in range(n)]
    stack = deque([(x, y, direct)])
    payDirect[x][y][0] = -500 # (0, 0)에서는 무조건 직선 도로인데, 코너로 측정되므로 빼준다.

    while stack:
        x, y, d = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if i == d and payDirect[x][y][0] + 100 < payDirect[nx][ny][0]:
                    payDirect[nx][ny][0] = payDirect[x][y][0] + 100
                    payDirect[nx][ny][1] = i
                    stack.append((nx, ny, i))
                elif payDirect[x][y][0] + 600 < payDirect[nx][ny][0]:
                    payDirect[nx][ny][0] = payDirect[x][y][0] + 600
                    payDirect[nx][ny][1] = i
                    stack.append((nx, ny, i))
                # pay는 같은데 방향은 다르면 stack에 추가한다.(직선)
                elif i == d and payDirect[x][y][0] + 100 == payDirect[nx][ny][0] and payDirect[nx][ny][1] != i:
                    payDirect[nx][ny][1] = i
                    stack.append((nx, ny, i))
                # pay는 같은데 방향이 다르면 stack에 추가한다.(코너)
                elif payDirect[x][y][0] + 600 == payDirect[nx][ny][0] and payDirect[nx][ny][1] != i:
                    payDirect[nx][ny][1] = i
                    stack.append((nx, ny, i))

    return payDirect[n-1][n-1][0]

'''

# 시간 초과
'''
<풀이 방법>
- DFS, 백트래킹
- 직선 100
- 코너 100 + 500
- 전달할 것: x, y, board, n(board 크기), 비용, 현재 방향, visited
'''
'''
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 백트래킹
# 전역변수로 선언하고, 이보다 큰 payment가 되면 탐색을 관둔다. (시간 초과 때문에)
result = 1000000000000

def dfs(x, y, board, n, payment, direct, visited):
    if x == n-1 and y == n-1:
        return payment
    
    global result
    if result < payment:
        return payment

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
            if i == direct:
                visited[nx][ny] = True
                result = min(result, dfs(nx, ny, board, n, payment+100, i, visited))
                visited[nx][ny] = False
            else:
                visited[nx][ny] = True
                result = min(result, dfs(nx, ny, board, n, payment+600, i, visited))
                visited[nx][ny] = False
    
    return result

def solution(board):
    answer = 0
    
    board = [[0] * 25 for _ in range(25)]
    n = len(board)
    
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    return dfs(0, 0, board, n, 0, -1, visited) - 500 # 처음 시작할 때 코너비용으로 들어간다.
'''