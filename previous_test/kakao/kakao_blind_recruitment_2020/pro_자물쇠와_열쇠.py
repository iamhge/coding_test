'''
<오답 노트>
- lock이 모두 0인 경우의 error handling을 하지 않았다.
'''

# g1의 startX, startY 좌표부터 g2에 해당하는 부분이 들어맞는지 return
def sameGrid(startX, startY, g1, g2):
    for i in range(len(g2)):
        for j in range(len(g2[0])):
            if g1[startX+i][startY+j] != g2[i][j]:
                return False
    return True

# 열 수 있는지 확인
def canOpen(key, lock):
    km = len(key)
    kn = len(key[0])
    lm = len(lock)
    ln = len(lock[0])
    
    if lm > km or ln > km:
        return False
    
    if lm == 0:
        return False
    
    for startX in range(km-lm+1):
        for startY in range(kn-ln+1):
            # lock 을 key[startX][startY] 부터 맞는지 탐색한다.
            if sameGrid(startX, startY, key, lock):
                return True
                
    return False

# 유의미한 직사각형 부분만 남긴다.
def cut(n, find, grid):
    coordinate = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == find:
                coordinate.append([i, j])
    
    if coordinate == []:
        return [[]]
    
    startX = min(coordinate, key = lambda x: x[0])[0]
    endX = max(coordinate, key = lambda x: x[0])[0]
    startY = min(coordinate, key = lambda x: x[1])[1]
    endY = max(coordinate, key = lambda x: x[1])[1]
    
    cutGrid = [[0] * (endY-startY+1) for _ in range(endX-startX+1)]
    
    for x, y in coordinate:
        cutGrid[x-startX][y-startY] = 1
    
    return cutGrid

# 회전한다.
def spin(grid):
    m = len(grid)
    n = len(grid[0])
    
    spinned = [[0]*m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            spinned[j][m-i-1] = grid[i][j]
    
    return spinned

def printGrid(grid):
    for g in grid:
        print(g)
    print()

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    cutKey = cut(m, 1, key)
    cutLock = cut(n, 0, lock)
    printGrid(cutLock)
    for _ in range(4):
        cutKey = spin(cutKey)
        if canOpen(cutKey, cutLock):
            return True
    
    return False