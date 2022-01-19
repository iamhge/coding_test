# 방문 길이
'''
<풀이 방법>
  1) 현재 좌표와 이동할 방향이 기록되어있지 않다면, 처음 걸어본 길이다.
    1-1) 현재 좌표와 이동할 방향을 기록한다.
      ex) ((0, 0), 'R')
  2) 이동 후, 이동한 좌표에서 지난 좌표로 돌아가는 방향을 기록한다.
<주의 사항>
  ※ 캐릭터가 이미 지난 길을 제외해야하므로 각 좌표에서 양방향으로 기록해야한다.
    ex) (0, 0)에서 (0, 1) 으로 이동한다면 ((0, 0), 'R'), ((0, 1), 'L') 과 같이 두 개가 기록된다.
  ※ 이동 후에도 같은 좌표라면 경로를 기록하지 않는다.
     해당 방향에 길이 없다는 의미이기 때문이다.
'''
# U R D L
commands = ["U", "R", "D", "L"]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def Coordinate(prev, command):
    ci = commands.index(command) # command index
    x, y = prev
    if 0 <= x + dx[ci] <= 10: x += dx[ci]
    if 0 <= y + dy[ci] <= 10: y += dy[ci]
        
    return (x, y)

def solution(dirs):
    answer = 0
    nowC = (0, 0) # 원점
    footPrint = []
    
    for i in range(len(dirs)):
        nextC = Coordinate(nowC, dirs[i]) # 이동할 좌표
        if nextC == nowC: continue # 이동 후에도 같은 좌표라면 경로를 기록하지 않는다.
        
        if (nowC, dirs[i]) not in footPrint:
            answer += 1
            footPrint.append((nowC, dirs[i])) # 현재 좌표에서 이동할 경로 기록
        
        nowC = nextC # 좌표 이동
        footPrint.append((nowC, commands[commands.index(dirs[i]) - 2])) # 이동한 좌표에서 이전 좌표로 가는 경로 기록 (길의 방향을 모두 따진다.)
        
    return answer

# 다른 사람 코드
'''
<풀이 방법>
  - 집합을 통해 간결하게 코딩
  - 아래 코드에서 s는 내 코드에서의 footPrint와 같은 역할.
  - 이동한 좌표가 범위를 벗어나면 아예 s에 넣지 않는 방식으로, 내 코드보다 검사할 것이 적게 보인다.
'''
'''
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
'''

# 오답
'''
# U D R L
commands = ["U", "D", "R", "L"]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def Coordinate(prev, command):
    ci = commands.index(command) # command index
    x, y = prev
    if -5 <= x + dx[ci] <= 5: x += dx[ci]
    if -5 <= y + dy[ci] <= 5: y += dy[ci]
        
    return (x, y)
    
def solution(dirs):
    answer = 0
    footPrint = [(0, 0)]
    
    for i in range(len(dirs)):
        nowC = footPrint[i]
        nextC = Coordinate(nowC, dirs[i])
        footPrint.append(nextC)
        
        if nowC == nextC:
            continue
        
        # footPrint에서 now 좌표의 index list
        indexList = list(filter(lambda x: footPrint[x] == nowC, range(len(footPrint)-2)))
        
        for index in indexList:
            if nextC == footPrint[index + 1]:
                break
            elif index >= 1 and nextC == footPrint[index - 1]:
                break
        else:
            answer += 1

    return answer
'''