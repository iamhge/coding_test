# 사라지는 발판
'''
<풀이 방법>
- 프로세스
    1) if 현재 서있던 발판이 사라진 경우: 패배
    2) if 움직일 수 없는 경우: 패배
    3) 이동
    4) 이전 발판을 제거한다.
- 최적의 플레이..?
    이기는 쪽은 턴을 최소화
    지는 쪽은 턴을 최대화
<참고 링크 1>
2022 카카오 신입 공채 1차 온라인 코딩테스트 for Tech developers 문제해설
: https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/
    <참고 내용>
    - 이 문제에서는 게임판의 상태에 따라 이번에 움직여야 하는 플레이어가 이길 수 있는지, 질 수밖에 없는지를 판단하고 판단한 결과와 이동한 횟수를 반환하는 재귀 함수를 구현해서 해결할 수 있습니다. 
    - 즉, 함수의 매개변수로 게임판의 상태, A의 위치, B의 위치 등을 넘겨주면, 이번 턴에 움직여야 하는 플레이어의 승패 여부와 총 이동 횟수를 알려주는 함수입니다.
    - 함수를 호출한 결과를 종합해 ‘이길 수 있는 방법이 있는지’, ‘질 수밖에 없는지’를 구할 수 있습니다.
<참고 링크 2>
2022 카카오 코딩테스트 lv.3 사라지는 발판 파이썬
: https://sujeng97.tistory.com/36
    <참고 내용>
    - 따라서 재귀를 돌때 만약 이길 수 있다면, 최단경로를 리턴해주고 만약 진다면 최대경로를 리턴해준다.
<소감>
- 너무 어려운 문제...
- 재귀 구현까지는 쉬웠지만, 최적의 플레이가 이해가지 않아 결국 해설을 찾아보았다.
- 이길 가능성이 있다 vs 질 수 밖에 없다 라는 아이디어를 떠올리는 것이 관건인 듯 하다.
'''
INF = 25

dx = [1, -1, 0, 0] # 행
dy = [0, 0, 1, -1] # 열

# return: turn의 플레이어가 이길 수 있는지 여부, 턴 횟수
def move(m, n, nowBoard, turn, loc, count):
    x, y = loc[turn]
    
    # if 현재 서있던 발판이 사라진 경우: 패배
    if nowBoard[x][y] == 0:
        return False, count
    
    loseResult = -1
    winResult = INF
    canMove = False
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n and nowBoard[nx][ny] == 1:
            canMove = True
            
            loc[turn] = [nx, ny] # 이동
            nowBoard[x][y] = 0 # 이전 발판 제거
            
            # 1-turn -> turn 변경
            lose, res = move(m, n, nowBoard, 1-turn, loc, count+1)
        
            # lose: 상대가 이길 방법이 있으면(True 반환되면) 지금 턴의 플레이어는 최대한 오래 살아야한다.
            if lose:
                loseResult = max(loseResult, res)
            # 상대가 질 수 밖에 없으면(False 반환되면) 지금 턴의 플레이어는 최소한의 턴으로 이겨야한다.
            else:
                winResult = min(winResult, res)
            
            nowBoard[x][y] = 1
            loc[turn] = [x, y]
            
    # if 움직일 수 없는 경우: 패배
    if not canMove:
        return False, count
    
    # 이길 가능성이 있는 경우
    if winResult != INF:
        return True, winResult
    # 이길 가능성이 없는 경우
    return False, loseResult

def printBoard(board):
    for i in range(len(board)):
        print(board[i])
    print()
        
def solution(board, aloc, bloc):
    m = len(board)
    n = len(board[0])
    loc = [aloc, bloc]
    return move(m, n, board, 0, loc, 0)[1]
    