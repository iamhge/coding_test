# 구슬 탈출 2
import sys
import copy
# 좌 우 상 하 (0 1 2 3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def printBaord(board):
    for b in board:
        print(b)
    print()

def incline(direct, board, rx, ry, bx, by):
    nrx = rx + dx[direct]
    nry = ry + dy[direct]
    nbx = bx + dx[direct]
    nby = by + dy[direct]
    # R
    board[ry][rx] = '.'
    while board[nry][nrx] == '.':
        # 이동
        rx = nrx
        ry = nry

        # 다음 위치
        nrx = rx + dx[direct]
        nry = ry + dy[direct]

    if board[nry][nrx] != 'O':
        board[ry][rx] = 'R'
    # printBaord(board)

    # B
    board[by][bx] = '.'
    while board[nby][nbx] == '.':
        # 이동
        bx = nbx
        by = nby

        # 다음 위치
        nbx = bx + dx[direct]
        nby = by + dy[direct]

    if board[nby][nbx] != 'O':
        board[by][bx] = 'B'
    # printBaord(board)

    # B에 가로막혀서 R이 이동하지 못했을 경우 다시 R 이동
    if board[nry][nrx] != '#':
        board[ry][rx] = '.'
        while board[nry][nrx] == '.':
            # 이동
            rx = nrx
            ry = nry

            # 다음 위치
            nrx = rx + dx[direct]
            nry = ry + dy[direct]
        if board[nry][nrx] != 'O':
            board[ry][rx] = 'R'
    # printBaord(board)

    if board[nby][nbx] == 'O':
        return board, rx, ry, nbx, nby
    elif board[nry][nrx] == 'O':
        return board, nrx, nry, bx, by

    return board, rx, ry, bx, by

cnt = 11
def DFS(board, rx, ry, bx, by, depth, visited):
    global cnt

    if depth > 10 or board[by][bx] == 'O':
        return

    if board[ry][rx] == 'O':
        cnt = min(cnt, depth)
        return

    for i in range(4):
        nboard, nrx, nry, nbx, nby = incline(i, copy.deepcopy(board), rx, ry, bx, by)
        if [nrx, nry, nbx, nby] not in visited:
            visited.append([nrx, nry, nbx, nby])
            DFS(nboard, nrx, nry, nbx, nby, depth + 1, copy.deepcopy(visited))
            visited.pop()

    return

def solution(board, rx, ry, bx, by):
    global cnt
    DFS(copy.deepcopy(board), rx, ry, bx, by, 0, [])
    if cnt > 10:
        print(-1)
    else:
        print(cnt)

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    board = []

    for i in range(N):
        board.append(list(input().rstrip()))
        if 'R' in board[i]:
            ry, rx = (i, board[i].index('R'))
        if 'B' in board[i]:
            by, bx = (i, board[i].index('B'))

    solution(copy.deepcopy(board), rx, ry, bx, by)

main()