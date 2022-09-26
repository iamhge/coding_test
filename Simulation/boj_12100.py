# 2048 (Easy)
'''
<풀이 방법>
  - 그냥... 냅다.... recursion...
<소감>
  - simulation은 정말정말 문제를 잘 읽고 테스트 케이스를 생각하는 게 중요하다.
    명심 명심 명심 x 10000
'''
import sys
import copy

input = sys.stdin.readline

def move(N, board, direct):
    # 상
    if direct == 0:
        for i in range(N):
            col = []
            for j in range(N):
                if board[j][i] != 0:
                    if col == []:
                        col.append(board[j][i])
                    elif col[-1] == board[j][i]:
                        col[-1] *= -2 # 여러번 합쳐지는 것 방지 위해 -(minus)로
                    else:
                        col.append(board[j][i])
            col.extend([0] * (N - len(col)))
            for j in range(N):
                board[j][i] = abs(col[j])
    # 하
    elif direct == 1:
        for i in range(N):
            col = []
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    if col == []:
                        col.append(board[j][i])
                    elif col[-1] == board[j][i]:
                        col[-1] *= -2
                    else:
                        col.append(board[j][i])
            col.extend([0] * (N - len(col)))
            for j in range(N):
                board[N-1-j][i] = abs(col[j])
    # 좌
    elif direct == 2:
        for i in range(N):
            row = []
            for j in range(N):
                if board[i][j] != 0:
                    if row == []:
                        row.append(board[i][j])
                    elif row[-1] == board[i][j]:
                        row[-1] *= -2
                    else:
                        row.append(board[i][j])
            row.extend([0] * (N - len(row)))
            for j in range(N):
                board[i][j] = abs(row[j])
    # 우
    else:
        for i in range(N):
            row = []
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    if row == []:
                        row.append(board[i][j])
                    elif row[-1] == board[i][j]:
                        row[-1] *= -2
                    else:
                        row.append(board[i][j])
            row.extend([0] * (N - len(row)))
            for j in range(N):
                board[i][N-1-j] = abs(row[j])
    # for b in board:
    #     print(b)
    # print()
    return board

def solution(N, board, cnt):
    if cnt >= 5:
        answer = -1
        for b in board:
            answer = max(answer, max(b))
        return answer

    answer = -1
    for direct in range(4):
        newBoard = move(N, copy.deepcopy(board), direct)
        answer = max(answer, solution(N, newBoard, cnt+1))

    return answer

def main():
    N = int(input().rstrip())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    print(solution(N, board, 0))

main()

# 다른 사람 코드
'''
<풀이 방법>
  - 전체적인 틀은 내 풀이와 비슷하나, 구체적인 부분이 다르다.
    1) 함수를 여러겹 사용하면서 x, y 방향을 변수로 처리해줬다. 더 객체지향적인 방법.
    2) get, merge 함수에서 큐를 사용했는데, 
       이 방법이 0과 여러 번 합쳐지는 경우를 고려하지 않아도 된다.
'''
'''
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()

def get(i, j):
    if board[i][j]: # 0이 아닌 값이라면
        q.append(board[i][j]) # queue에 board의 값을 넣는다.
        board[i][j] = 0 # 처리가 된 빈 자리는 0으로 값 업데이트
        
def merge(i, j, di, dj): # row index, column index, y방향, x방향 
    while q:
        x = q.popleft() # 움직이려는 블록 값을 가져온다. FIFO 
        if not board[i][j]: # 0이라면 x를 그대로 놓는다.
            board[i][j] = x
        elif board[i][j] == x: # 값이 일치한다면
            board[i][j] = x*2 # 합쳐지므로 2배로 증가
            i, j = i+di, j+dj # 탐색 자리 이동
        else: # 값이 일치하지 않으면
            i, j = i+di, j+dj # 이동 후
            board[i][j] = x # x를 놓는다

def move(k):
    # board[i][j]
    if k == 0: # 위로 이동, 블락들이 위로 모두 이동하면 row index는 0
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0) # row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
    elif k == 1: # 아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0) # row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
    elif k == 2: # 오른쪽으로 이동, column index는 0
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1) # column 인덱스 증가 오른쪽으로 이동
    else: # 왼쪽으로 이동, column index는 n-1
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1) # column 인덱스 감소 왼쪽으로 이동
            
def solve(count):
    global board, answer
    if count == 5: # 최대 5번까지 움직였다면
        for i in range(n):
            answer = max(answer, max(board[i])) # 가장 큰 값이 answer
        return
    b = [x[:] for x in board] # 방향을 바꾸기 전에 원래의 보드를 기억해야 한다.
    
    for k in range(4): # 4방향으로 움직인다.
        move(k) # 움직인다.
        solve(count+1) # 재귀적으로 호출한다.
        board = [x[:] for x in b]

solve(0)
print(answer)
'''

# 틀린 풀이
'''
<반례>
4
2 2 4 16
0 0 0 0
0 0 0 0
0 0 0 0
위 상태에서 왼쪽으로 한 번 이동하면

4 4 16 0
0 0 0 0
0 0 0 0
0 0 0 0
가 되어야 하는데 

아래 코드는 

8 16 0 0
0 0 0 0
0 0 0 0
0 0 0 0
이렇게 된다.
'''
'''
import sys
import copy

input = sys.stdin.readline

def move(N, board, direct):
    # 상
    if direct == 0:
        for i in range(N):
            col = []
            for j in range(N):
                if board[j][i] != 0:
                    if col == []:
                        col.append(board[j][i])
                    elif col[-1] == board[j][i]:
                        col[-1] *= 2
                    else:
                        col.append(board[j][i])
            col.extend([0] * (N - len(col)))
            for j in range(N):
                board[j][i] = col[j]
    # 하
    elif direct == 1:
        for i in range(N):
            col = []
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    if col == []:
                        col.append(board[j][i])
                    elif col[-1] == board[j][i]:
                        col[-1] *= 2
                    else:
                        col.append(board[j][i])
            col.extend([0] * (N - len(col)))
            for j in range(N):
                board[N-1-j][i] = col[j]
    # 좌
    elif direct == 2:
        for i in range(N):
            row = []
            for j in range(N):
                if board[i][j] != 0:
                    if row == []:
                        row.append(board[i][j])
                    elif row[-1] == board[i][j]:
                        row[-1] *= 2
                    else:
                        row.append(board[i][j])
            row.extend([0] * (N - len(row)))
            for j in range(N):
                board[i][j] = row[j]
    # 우
    else:
        for i in range(N):
            row = []
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    if row == []:
                        row.append(board[i][j])
                    elif row[-1] == board[i][j]:
                        row[-1] *= 2
                    else:
                        row.append(board[i][j])
            row.extend([0] * (N - len(row)))
            for j in range(N):
                board[i][N-1-j] = row[j]
    
    # for b in board:
    #     print(b)
    # print()
    return board

def solution(N, board, cnt):
    if cnt >= 5:
        answer = -1
        for b in board:
            answer = max(answer, max(b))
        return answer

    answer = -1
    for direct in range(4):
        newBoard = move(N, copy.deepcopy(board), direct)
        answer = max(answer, solution(N, newBoard, cnt+1))

    return answer

def main():
    N = int(input().rstrip())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    move(N, board, 2)

    for b in board:
        print(b)
    print(solution(N, board, 0))

main()
'''