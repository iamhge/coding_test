# 아이템 줍기
'''
<풀이 방법>
- 무조건 시계방향으로 방향성을 설정한다.
- mymap에는 방향성을 저장한다.
  mymap[y][x]에는 다음 위치로 갈 수 있는 방향성을 저장한다.
  좌표 찍으면 직사각형 모양은 이런 모양
    우 우 우 하
    상      하
    상      하
    상 좌 좌 좌
- mymap 초기화 시, 다른 직사각형과 마주칠 경우 방향성은 다음과 같은 우선순위를 가진다.
  우선 순위가 높은 방향성이 mymap에 저장된다.
  상 < 우
  우 < 하
  하 < 좌
  좌 < 상
- 방향성의 우선순위는 항상 시계방향으로 돌기 때문에 위와 같이 설정된다.
 '''
# 상 우 하 좌
dx = [0, 1, 0, -1] # 열
dy = [1, 0, -1, 0] # 행

# -1 = 빈자리, 0~3 = 방향성(시계방향 기준)
mymap = [[-1]*51 for _ in range(51)]

def move(root, target):
    cnt = 0
    x, y = root
    
    while (x, y) != target:
        d = mymap[y][x]
        x = x + dx[d]
        y = y + dy[d]
        cnt += 1
        
    return cnt
        
def draw(rec):
    global mymap
    # 좌상 x1 y2, 우상 x2 y2
    # 좌하 x1 y1, 우하 x2 y1
    x1, y1, x2, y2 = rec
    
    # 상
    for i in range(y1, y2): # 행
        # 만난 직사각형이 좌 방향인 경우 -> 기존 직사각형의 방향성이 우선된다.
        if mymap[i][x1] != 3:
            mymap[i][x1] = 0
    # 우
    for j in range(x1, x2):
        # 만난 직사각형이 상 방향인 경우 -> 기존 직사각형의 방향성이 우선된다.
        if mymap[y2][j] != 0:
            mymap[y2][j] = 1
            
    # 하
    for i in range(y2, y1, -1): # 행
        # 만난 직사각형이 우 방향인 경우 -> 기존 직사각형의 방향성이 우선된다.
        if mymap[i][x2] != 1:
            mymap[i][x2] = 2
    
    # 좌
    for j in range(x2, x1, -1): # 열
        # 만난 직사각형이 하 방향인 경우 -> 기존 직사각형의 방향성이 우선된다.
        if mymap[y1][j] != 2:
            mymap[y1][j] = 3
            
def printmap():
    for i in range(10, -1, -1):
        for j in range(0,10):
            if mymap[i][j] == -1:
                print('_', end=" ")
            else:
                print(mymap[i][j], end=" ")
        print()
    print()
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    for i in range(len(rectangle)):
        draw(rectangle[i])
        
    c2i = move((characterX, characterY), (itemX, itemY))
    i2c = move((itemX, itemY), (characterX, characterY))
    
    return min(c2i, i2c)

