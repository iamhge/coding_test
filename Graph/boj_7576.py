# 토마토
'''
<아이디어>
  BFS 이용해서 한칸씩 늘리되, 걸린 시간(일 수)를 기입한다.
<참고>
  Python 2차원 배열의 최대값, 최소값 찾기
   : https://devbull.xyz/python-2caweon-baeyeolyi-coedaegabs-coesogabs-cajgi/
     토마토 모두 익지 못하는 상황 제외하고 day만 출력할 때는 아래 코드 쓰면 됐음.
     이 문제는 어차피 2중 for문 돌려야 해서 쓰지 않음.
     day = max(map(max, WareHouse)) - 1

'''
import sys
from collections import deque

def Spread(M: int, N: int, Map: list, root: list):
    queue = deque(root)
    # [상, 하, 좌, 우]
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x_ = x + dx[i] # x prime
            y_ = y + dy[i] # y prime
            if 0 <= x_ < N and 0 <= y_ < M and Map[x_][y_] == 0:
                Map[x_][y_] = Map[x][y] + 1
                queue.append((x_, y_))
    
    return Map

M, N = map(int, sys.stdin.readline().split())
WareHouse = []
root = []
day = 0
NotRipe = 0

for _ in range(N):
    WareHouse.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if WareHouse[i][j] == 1:
            root.append((i, j))

WareHouse = Spread(M, N, WareHouse, root)

for i in range(N):
    for j in range(M):
        if WareHouse[i][j] == 0:
            NotRipe += 1
        day = max(WareHouse[i][j] - 1, day)

if NotRipe == 0:
    print(day)
else:
    print("-1")