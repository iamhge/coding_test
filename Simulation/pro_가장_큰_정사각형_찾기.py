# 가장 큰 정사각형 찾기
'''
array의 값은 위->아래, 왼->오로 탐색하면서
해당 자리가 만들 수 있는 최대 정사각형의 변의 길이
0번째 행과 열은 모두 board와 같은 값
0 1 1 1
1 
1
0 

if board[n][m] == 1:
    a[n][m] = min(a[n-1][m-1], a[n-1][m], a[n][m-1]) + 1
else:
    a[n][m] = 0
0 1 1 1
1 1 2 2
1 2 2 3
0 0 1 0
'''
def solution(board):
    sideLen = 0
    N = len(board) # 행
    M = len(board[0]) # 열
    a = list([0 for _ in range(M)] for _ in range(N))
    
    a[0] = board[0]
    for n in range(N):
        a[n][0] = board[n][0]

    # 행 또는 열의 크기가 1일 때
    # board에 1이 하나라도 있으면 답이 1, 없으면 답이 0으로 정해진다.
    if N < 2 or M < 2:
        for i in board:
            for j in i:
                if j == 1:
                    return 1
        return 0
    
    for n in range(1, N):
        for m in range(1, M):
            if board[n][m] == 1:
                a[n][m] = min(a[n-1][m-1], a[n-1][m], a[n][m-1]) + 1
                sideLen = max(sideLen, a[n][m])
            else:
                a[n][m] = 0
    
    return sideLen * sideLen