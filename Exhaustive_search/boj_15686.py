# 치킨 배달
import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    Map = []
    for _ in range(N):
        Map.append(list(map(int, input().split())))

    chicken = [] # 치킨집 좌표
    house = [] # 집 좌표

    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                chicken.append((i, j))
            elif Map[i][j] == 1:
                house.append((i, j))

    chickenLen = [[] for _ in range(len(chicken))] # 각 치킨집의 치킨 거리 list
    i = 0
    for r1, c1 in chicken:
        for r2, c2 in house:
            chickenLen[i].append(abs(r1 - r2) + abs(c1 - c2))
        i += 1

    result = 4*N*N # 집의 개수 < 2*N, 치킨 거리 <= 2*N
    for picked in list(combinations(chickenLen, M)):
        pickedCL = []
        for i in range(len(house)):
            pickedCL.append(min(picked[j][i] for j in range(M)))
        result = min(sum(pickedCL), result)
    
    print(result)

if __name__=="__main__":
    main()

# 다른 사람 코드
# combination 함수 쓰지 않고, 조합 알고리즘 사용
'''
import sys

input = sys.stdin.readline

n,m = list(map(int,input().strip().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int,input().strip().split())))
house = []
chicken = []
for i in range(n):
    for j in range(n):
        v = grid[i][j]
        if v == 1:
            house.append([i,j])
        elif v == 2:
            chicken.append([i,j])
distance = []
for h in house:
    h_x,h_y = h
    h_l = []
    for c in chicken:
        c_x,c_y = c
        h_l.append(abs(h_x-c_x)+abs(h_y-c_y))
    distance.append(h_l)
distance = list(zip(*distance))
def check(select=[],index=-1):
    if len(select) == m:
        values = list(zip(*select))
        w = 0
        for v in values:
            w += min(v)
        return w
    if index == len(distance):
        return 999999
    #순서는 상관 없음
    ret = 99999999
    for i in range(index+1,len(distance)):
        select.append(distance[i])
        ret = min(ret,check(select,i))
        select.pop(-1)
    return ret
    
    
print(check())
'''