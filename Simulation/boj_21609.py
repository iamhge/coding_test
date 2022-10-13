# 상어 중학교
'''
<풀이 방법>
  - 블록을 Grouping 할 때 주의할 점
    1) 무지개 블록의 경우, 여러 그룹에 속할 수 있다.
    2) 그룹에 속한 블록의 개수가 2보다 크거나 같아야 하는데, 이 때 무조건 일반블록이 2개 이상이어야만 하는 것은 아니다. 반례 -> 예제3
'''

from collections import deque, defaultdict

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = 0
blockMap = []

def canMakeBlockGroup(x, y, target):
    global n, blockMap

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if blockMap[nx][ny] == target or blockMap[nx][ny] == 0:
                return True
    return False


def findGroup(visited, root, target):
    global n, blockMap

    group = []
    queue = deque([root])
    standard = (n, n)
    rainbowNum = 0

    while queue:
        x, y = queue.popleft()

        # 기준 블록은 무지개 블록이 아니다.
        # 기준 블록은 행의 번호가 가장 작은 블록, 그 중에서도 열의 번호가 가장 작은 블록이다.
        if blockMap[x][y] != 0 and (x < standard[0] or (x == standard[0] and y < standard[1]) ):
            standard = (x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) in group:
                    continue
                if blockMap[nx][ny] == target or blockMap[nx][ny] == 0:
                    queue.append((nx, ny))
                    group.append((nx, ny))
                    visited[x][y] = True
                    if blockMap[nx][ny] == 0:
                        rainbowNum += 1
                        visited[x][y] = False


    return visited, group, standard, rainbowNum


def grouping():
    global n, blockMap

    visited = [[False for __ in range(n)] for _ in range(n)]
    groups = defaultdict(list)  # key = 기준 블록, value = 그룹에 포함된 블록들의 좌표
    rainbows = defaultdict(int)  # key = 기준 블록, value = 그룹에 포함된 무지개 블록 수

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if blockMap[i][j] > 0:
                if not canMakeBlockGroup(i, j, blockMap[i][j]):
                    continue
                visited, group, standard, rainbowNum = findGroup(visited, (i, j), blockMap[i][j])
                groups[standard] = group
                rainbows[standard] = rainbowNum

    return groups, rainbows


def getBiggestGroup(groups, rainbows):
    global n

    biggestStan = (n, n)
    biggestLen = 0

    for key, value in groups.items():
        if len(value) > biggestLen:
            biggestStan = key
            biggestLen = len(value)
        elif len(value) == biggestLen:
            # 1) 무지개가 더 많은
            if rainbows[key] > rainbows[biggestStan]:
                biggestStan = key
                biggestLen = len(value)
            elif rainbows[key] == rainbows[biggestStan]:
                # 2) 기준 블록의 행이 더 큰
                if key[0] > biggestStan[0]:
                    biggestStan = key
                    biggestLen = len(value)
                elif key[0] == biggestStan[0]:
                    # 3) 기준 블록의 열이 더 큰
                    if key[1] > biggestStan[1]:
                        biggestStan = key
                        biggestLen = len(value)

    return biggestStan


def popBlockGroup(group):
    global blockMap

    for x, y in group:
        blockMap[x][y] = -2


def gravity():
    global n, blockMap

    fall = deque([])
    for j in range(n):  # 열
        floor = n-1
        for i in range(n-1, -1, -1):  # 행
            if blockMap[i][j] == -1:
                while fall:
                    blockMap[floor][j] = fall.popleft()
                    floor -= 1
                floor = i - 1
            elif blockMap[i][j] == -2:
                continue
            else:
                fall.append(blockMap[i][j])
                blockMap[i][j] = -2

        while fall:
            blockMap[floor][j] = fall.popleft()
            floor -= 1


def rotate():
    global n, blockMap

    rotatedMap = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotatedMap[i][j] = blockMap[j][n-1-i]

    blockMap = rotatedMap


def printBlockMap():
    global n, blockMap
    for i in range(n):
        for j in range(n):
            if blockMap[i][j] == -2:
                print(' _', end=' ')
            else:
                if blockMap[i][j] >= 0:
                    print(' ', end='')
                print(blockMap[i][j], end=' ')
        print()
    print()


def main():
    global n, blockMap
    n, m = map(int, input().split())
    for _ in range(n):
        blockMap.append(list(map(int, input().split())))

    # printBlockMap()
    score = 0

    while 1:
        # 1
        groups, rainbows = grouping()
        if len(groups) == 0:
            break
        biggestStan = getBiggestGroup(groups, rainbows)
        biggestGroup = groups[biggestStan]

        # print(groups)
        # printBlockMap()

        # 2
        popBlockGroup(biggestGroup)
        score += len(biggestGroup) ** 2

        # print("블록 제거 후")
        # printBlockMap()

        # 3
        gravity()

        # print("중력 작용")
        # printBlockMap()

        # 4
        rotate()

        # print("회전")
        # printBlockMap()

        # 5
        gravity()

        # print("중력 작용")
        # printBlockMap()
        # print(len(biggestGroup) ** 2)

    return score


print(main())


'''
<오답 노트>
  1) rainbow 블록은 다시 방문할 수 있는 것을 알고 있었으면서 처리를 잘못해줬다.
  2) 기준 블록은 일반 블록이어야 한다.
  - 실제 테스트 볼 때는 이런 실수 하지않게 집중 빡!! 하자..!!
<반례> 
3 3
0 2 2
3 1 -1
3 -1 -1
-> 기준 블록을 프린트해보면 rainbow 블록이 기준 블록이 된다.
'''
'''
from collections import deque, defaultdict

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = 0
blockMap = []

def canMakeBlockGroup(x, y, target):
    global n, blockMap

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if blockMap[nx][ny] == target or blockMap[nx][ny] == 0:
                return True
    return False


def findGroup(blockGroup, groupNum, root, target):
    global n, blockMap

    visited = []
    queue = deque([root])
    standard = (n, n)
    rainbowNum = 0

    while queue:
        x, y = queue.popleft()
        blockGroup[x][y].append(groupNum)
        if x < standard[0] or (x == standard[0] and y < standard[1]):
            standard = (x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) in visited:
                    continue
                if blockMap[nx][ny] == target or blockMap[nx][ny] == 0:
                    if blockMap[nx][ny] == 0:
                        rainbowNum += 1
                    queue.append((nx, ny))
                    visited.append((nx, ny))

    return blockGroup, visited, standard, rainbowNum


def grouping():
    global n, blockMap

    blockGroup = [[[] for __ in range(n)] for _ in range(n)]
    groupNum = 1
    groups = defaultdict(list)  # key = 기준 블록, value = 그룹에 포함된 블록들의 좌표
    rainbows = defaultdict(int)  # key = 기준 블록, value = 그룹에 포함된 무지개 블록 수

    for i in range(n):
        for j in range(n):
            if blockGroup[i][j]:
                continue
            if blockMap[i][j] > 0:
                if not canMakeBlockGroup(i, j, blockMap[i][j]):
                    continue
                blockGroup, group, standard, rainbowNum = findGroup(blockGroup, groupNum, (i, j), blockMap[i][j])
                groups[standard] = group
                rainbows[standard] = rainbowNum
                groupNum += 1

    return groups, rainbows


def getBiggestGroup(groups, rainbows):
    global n

    biggestStan = (n, n)
    biggestLen = 0

    for key, value in groups.items():
        if len(value) > biggestLen:
            biggestStan = key
            biggestLen = len(value)
        elif len(value) == biggestLen:
            # 1) 무지개가 더 많은
            if rainbows[key] > rainbows[biggestStan]:
                biggestStan = key
                biggestLen = len(value)
            elif rainbows[key] == rainbows[biggestStan]:
                # 2) 기준 블록의 행이 더 큰
                if key[0] > biggestStan[0]:
                    biggestStan = key
                    biggestLen = len(value)
                elif key[0] == biggestStan[0]:
                    # 3) 기준 블록의 열이 더 큰
                    if key[1] > biggestStan[1]:
                        biggestStan = key
                        biggestLen = len(value)

    return biggestStan


def popBlockGroup(group):
    global blockMap

    for x, y in group:
        blockMap[x][y] = -2


def gravity():
    global n, blockMap

    fall = deque([])
    for j in range(n):  # 열
        floor = n-1
        for i in range(n-1, -1, -1):  # 행
            if blockMap[i][j] == -1:
                while fall:
                    blockMap[floor][j] = fall.popleft()
                    floor -= 1
                floor = i - 1
            elif blockMap[i][j] == -2:
                continue
            else:
                fall.append(blockMap[i][j])
                blockMap[i][j] = -2

        while fall:
            blockMap[floor][j] = fall.popleft()
            floor -= 1


def rotate():
    global n, blockMap

    rotatedMap = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotatedMap[i][j] = blockMap[j][n-1-i]

    blockMap = rotatedMap


def printBlockMap():
    global n, blockMap
    for i in range(n):
        for j in range(n):
            if blockMap[i][j] == -2:
                print(' _', end=' ')
            else:
                if blockMap[i][j] >= 0:
                    print(' ', end='')
                print(blockMap[i][j], end=' ')
        print()
    print()


def main():
    global n, blockMap
    n, m = map(int, input().split())

    for _ in range(n):
        blockMap.append(list(map(int, input().split())))

    score = 0

    while 1:
        # print("------------------")
        # 1
        groups, rainbows = grouping()
        if len(groups) == 0:
            break
        biggestStan = getBiggestGroup(groups, rainbows)
        biggestGroup = groups[biggestStan]

        print(groups)
        # printBlockMap()

        # 2
        popBlockGroup(biggestGroup)
        score += len(biggestGroup) ** 2

        # print("블록 제거 후")
        # printBlockMap()

        # 3
        gravity()

        # print("중력 작용")
        # printBlockMap()

        # 4
        rotate()

        # print("회전")
        # printBlockMap()

        # 5
        gravity()

        # print("중력 작용")
        # printBlockMap()
        # print(len(biggestGroup) ** 2)

    return score

print(main())

'''