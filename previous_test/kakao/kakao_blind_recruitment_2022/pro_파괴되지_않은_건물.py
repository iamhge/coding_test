# 파괴되지 않은 건물
'''
* 해설 보고 풀이 했음
<풀이 방법>
  - 누적합
    : 변화 값을 저장해두었다가 나중에 한 번에 연산한다.
'''
def unbrokenBuilding(board):
    cnt = 0
    for b in board:
        for j in b:
            if j > 0 : cnt += 1
    return cnt

def doSkill(prefixSum, typ, r1, c1, r2, c2, degree):
    if typ == 1: # 적의 공격
        prefixSum[r1][c1] -= degree
        prefixSum[r1][c2+1] += degree
        prefixSum[r2+1][c2+1] -= degree
        prefixSum[r2+1][c1] += degree
    else: # 아군의 회복
        prefixSum[r1][c1] += degree
        prefixSum[r1][c2+1] -= degree
        prefixSum[r2+1][c2+1] += degree
        prefixSum[r2+1][c1] -= degree
    return prefixSum

def doPrefixSum(n, m, prefixSum):
    for i in range(n):
        for j in range(1, m):
            prefixSum[i][j] += prefixSum[i][j-1]
    for j in range(m):
        for i in range(1, n):
            prefixSum[i][j] += prefixSum[i-1][j]
    return prefixSum

def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    prefixSum = [[0] * (M+1) for _ in range(N+1)]
    
    for nowSkill in skill:
        prefixSum = doSkill(prefixSum, nowSkill[0], nowSkill[1], nowSkill[2], nowSkill[3], nowSkill[4], nowSkill[5])
        
    prefixSum = doPrefixSum(N+1, M+1, prefixSum)
    for i in range(N):
        for j in range(M):
            board[i][j] += prefixSum[i][j]
    
    return unbrokenBuilding(board)

# 정확성 통과, 효율성 실패 (시간 초과)
'''
def unbrokenBuilding(board):
    cnt = 0
    for b in board:
        for j in b:
            if j > 0 : cnt += 1
    return cnt

def doSkill(board, nowSkill):
    if nowSkill[0] == 1: # 적의 공격
        for r in range(nowSkill[1], nowSkill[3]+1):
            for c in range(nowSkill[2], nowSkill[4]+1):
                board[r][c] -= nowSkill[-1]
    else: # 아군의 회복
        for r in range(nowSkill[1], nowSkill[3]+1):
            for c in range(nowSkill[2], nowSkill[4]+1):
                board[r][c] += nowSkill[-1]
    return board

def solution(board, skill):
    answer = 0
    for s in skill:
        board = doSkill(board, s)
    return unbrokenBuilding(board)
'''