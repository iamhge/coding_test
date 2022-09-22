# 뱀
import sys
import copy
from collections import deque, defaultdict
input = sys.stdin.readline

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def printBoard(N, board, snake):
    b = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            if (i, j) in snake:
                b[i][j] = 8
        print(b[i])
    print()

def solution(N, board, L, route):
    snake = deque([(0, 0)]) # queue
    direct = 0
    nx = dx[direct]
    ny = dy[direct]
    seq = 1
    
    while 0 <= nx < N and 0 <= ny < N and (nx, ny) not in snake:
        x = nx
        y = ny

        # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        snake.append((x, y))
        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if board[x][y] == 1:
            board[x][y] -= 1
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        else:
            snake.popleft()

        if seq in route:
            # 방향 전환
            if route[seq] == 'L': # 왼쪽
                direct = (direct+3) % 4 
            else: # 오른쪽
                direct = (direct+1) % 4
        
        nx = x + dx[direct]
        ny = y + dy[direct]

        seq += 1
        
    return seq

def main():
    N = int(input().rstrip())
    K = int(input().rstrip())

    board = [[0] * N for _ in range(N)]
    for _ in range(K):
        apple = list(map(int, input().split()))
        board[apple[0]-1][apple[1]-1] = 1
    
    L = int(input().rstrip())

    route = defaultdict(str)
    for _ in range(L):
        tmp = list(input().split())
        route[int(tmp[0])] = (tmp[1])

    print(solution(N, board, L, route))

main()