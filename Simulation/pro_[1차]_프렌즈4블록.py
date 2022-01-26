import copy
dx = [1, 0, 1]
dy = [0, 1, 1]

def popBlock(n, m, board):
    for j in range(n):
        i = m-1
        while i >= 0:
            cnt = 0
            while board[i-cnt][j] == '_' or board[i-cnt][j] == '*':
                board[i-cnt][j] = '*' # 체크
                if i-cnt == 0: break
                cnt += 1
            for k in range(cnt):
                if i-k-cnt >= 0:
                    board[i-k][j] = board[i-k-cnt][j]
                    board[i-k-cnt][j] = '*'
            i -= 1
    return board

def solution(m, n, board):
    answer = 0
    popCnt = 1
    for i in range(m):
        board[i] = list(board[i])

    while popCnt != 0:
        popCnt = 0
        newBoard = copy.deepcopy(board)
        for i in range(m-1):
            for j in range(n-1):
                now = board[i][j]
                if now == '*': continue
                for k in range(3):
                    if now != board[i + dy[k]][j + dx[k]]:
                        break
                else: # 모두 같으면
                    newBoard[i][j] = '_'
                    for k in range(3):
                        newBoard[i + dy[k]][j + dx[k]] = '_'
        for i in range(m):
            popCnt += newBoard[i].count('_')
        answer += popCnt
        board = popBlock(n, m, newBoard)
            
    return answer