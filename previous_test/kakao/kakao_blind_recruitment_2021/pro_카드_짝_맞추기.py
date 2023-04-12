# 카드 짝 맞추기
'''
<주의 조건>
1) ctrl 키를 누르고 방향키를 누르는 것 != 그냥 방향키만 누르는 것
<풀이 방법>
- dfs로 1차 탐색 후
  bfs로 타겟에 대한 최소 키 입력 수를 구한다.
1) 오픈한 카드가 있는 경우 (dfs)
   - 오픈했던 카드와 같은 카드를 찾는다. (bfs)
2) 오픈한 카드가 없는 경우 (dfs)
   - 모든 카드에 대해 탐색한다. (bfs)
     가까운 카드가 최선의 선택이라는 보장이 없으므로.
<소감>
- 정말 너~무 오래걸렸다.
  처음에는 dfs 하나만 쓰면 되겠지 했으나, 그렇게 하면 너무 복잡하고 안풀렸다..
- 사실 풀고 나면 아이디어가 단순한데... 말로 표현이 안되네..
'''
import sys
sys.setrecursionlimit(1000000000)

from collections import deque

BOARD_SIZE = 4
INF = 1000000000000

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(board, x, y, direct):
    nx = x + dx[direct]
    ny = y + dy[direct]
    
    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
        x, y = nx, ny
    
    return x, y

def moveWithCtrl(board, x, y, direct):
    nx = x + dx[direct]
    ny = y + dy[direct]
    
    while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
        x, y = nx, ny
        if board[x][y] != 0:
            break
        nx += dx[direct]
        ny += dy[direct]
        
    return x, y

# target 카드의 좌표, target 카드로 가는 최소 키 입력 수
def findTarget(board, x, y, target):
    queue = deque([(x, y, 0)])
    visited = [(x, y)]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if board[x][y] == target:
            break

        for i in range(4):
            mx, my = move(board, x, y, i)
            if (mx, my) not in visited:
                queue.append((mx, my, cnt+1))
                visited.append((mx, my))
                
            mcx, mcy = moveWithCtrl(board, x, y, i)
            if (mcx, mcy) not in visited:
                queue.append((mcx, mcy, cnt+1))
                visited.append((mcx, mcy))
        
    return x, y, cnt

# tx, ty 좌표로 갈 동안 최소 키 입력 수
def howMany(board, x, y, tx, ty):
    queue = deque([(x, y, 0)])
    visited = [(x, y)]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == tx and y == ty:
            break

        for i in range(4):
            mx, my = move(board, x, y, i)
            if (mx, my) not in visited:
                queue.append((mx, my, cnt+1))
                visited.append((mx, my))
                
            mcx, mcy = moveWithCtrl(board, x, y, i)
            if (mcx, mcy) not in visited:
                queue.append((mcx, mcy, cnt+1))
                visited.append((mcx, mcy))
        
    return cnt

def dfs(board, x, y, count, openCard):
    # 모든 카드가 뒤집혔다면 종료한다.
    for line in board:
        if sum(line) > 0:
            break
    else:
        return count
    
    result = INF
    
    # 이미 오픈한 카드가 없는 경우
    if openCard == 0:
        # 모든 카드에 대한 경우의 수를 구한다.
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 0:
                    moveCnt = howMany(board, x, y, i, j)
                        
                    openCard = board[i][j]
                    board[i][j] = 0
                        
                    result = min(result, dfs(board, i, j, count+moveCnt+1, openCard))
                    
                    board[i][j] = openCard
            
    # 이미 오픈한 카드가 있는 경우
    else:
        nx, ny, moveCnt = findTarget(board, x, y, openCard)
        
        board[nx][ny] = 0
        
        result = min(result, dfs(board, nx, ny, count+moveCnt+1, 0))
        
        board[nx][ny] = openCard

    return result

def solution(board, r, c):
    return dfs(board, r, c, 0, 0)