# 주사위 굴리기
import sys
input = sys.stdin.readline

# _ 동 서 북 남
dx = [0, 0, 0, -1, 1] # 행
dy = [0, 1, -1, 0, 0] # 열

# 상 하 동 서 남 북
dice = {'top' : 0, 'bottom': 0, 'east': 0, 'west': 0, 'south': 0, 'north': 0}

row = ['top', 'east', 'bottom', 'west']
col = ['top', 'south', 'bottom', 'north']

# 다음 dice 전개도
def moveDice(direct, dice):
    # 동 (상 -> 동, 동 -> 하, 하 -> 서, 서 -> 상)
    if direct == 1:
        # print("동")
        changed = [] # dice의 상 동 하 서에 있는 숫자
        for i in row:
            changed.append(dice[i])
        for i in range(4): # 상 동 하 서 <- 이전 서 상 동 하
            dice[row[i]] = changed[i-1]

    # 서 (상 <- 동, 동 <- 하, 하 <- 서, 서 <- 상)
    elif direct == 2:
        # print("서")
        changed = [] # dice의 상 동 하 서에 있는 숫자
        for i in row:
            changed.append(dice[i])
        for i in range(4): # 서 상 동 하 <- 이전 상 동 하 서
            dice[row[i-1]] = changed[i]
    
    # 북 (상 <- 남, 남 <- 하, 하 <- 북, 북 <- 상)
    elif direct == 3:
        # print('북')
        changed = [] # dice의 상 남 하 북에 있는 숫자
        for i in col:
            changed.append(dice[i])
        for i in range(4): # 북 상 남 하 <- 이전 상 남 하 북
            dice[col[i-1]] = changed[i]

    # 남 (상 -> 남, 남 -> 하, 하 -> 북, 북 -> 상)
    else:
        # print('남')
        changed = [] # dice의 상 남 하 북에 있는 숫자
        for i in col:
            changed.append(dice[i])
        for i in range(4): # 상 남 하 북 <- 이전 북 상 남 하
            dice[col[i]] = changed[i-1]
    
    return dice
    
def solution(N, M, x, y, K, mymap, route):
    answer = []
    global dice
    for direct in route:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if not (0 <= nx < N and 0 <= ny < M): continue

        x = nx
        y = ny

        dice = moveDice(direct, dice)
        if mymap[x][y] == 0:
            mymap[x][y] = dice['bottom']
        else:
            dice['bottom'] = mymap[x][y]
            mymap[x][y] = 0
        # print("now :", x, y)
        # print(dice)
        # for m in mymap:
        #     print(m)
        # print()
        
        answer.append(dice['top'])
    return answer 

def main():
    N, M, x, y, K = map(int, input().split())
    mymap = []
    for _ in range(N):
        mymap.append(list(map(int, input().split())))
    route = list(map(int, input().split()))

    for num in solution(N, M, x, y, K, mymap, route):
        print(num)

main()