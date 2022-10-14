# 마법사 상어와 복제
'''
<소감>
  - 진~짜 오래 걸렸다.
  - 구현만 하면 되는데, 중간 중간 놓치거나 잘못 코딩하는 조건들 때문에 오류 잡느라 고생한다...
'''

n = 4
# 좌 좌상 상 우상 우 우하 하 좌하
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상 좌 하 우
directInt = {2: 1, 0: 2, 6: 3, 4: 4}
methods = []


# 냄새의 유효기간?이 줄어든다.
def smellGone(smell):
    for i in range(n):
        for j in range(n):
            if smell[i][j] >= 1:
                smell[i][j] -= 1
    return smell


# 상어의 이동 경로에 있는 물고기의 인덱스 리스트 반환
def countFish(shark, method, grid):
    nx = shark[0]
    ny = shark[1]
    fishesOnMethod = set()

    for direct in method:
        nx += dx[direct]
        ny += dy[direct]
        fishesOnMethod |= set(grid[nx][ny])

    return list(fishesOnMethod)


# 상어의 이동 방법 a가 b보다 사전 순으로 앞서면 True, b가 앞서(거나, 같으)면 False
def dictionaryFirst(a, b):
    aToInt = ''
    for direct in a:
        aToInt += str(directInt[direct])

    bToInt = ''
    for direct in b:
        bToInt += str(directInt[direct])

    if int(aToInt) < int(bToInt):
        return True
    return False


# 상어 이동 방법의 순열 반환
def sharkMovePermutations(x, y, perm, remain):
    global methods
    if remain == 0:
        # methods.append(perm) 으로 하면 안된다.
        # 재귀함수 내에서 perm이 바뀌면, 전역변수 리스트 안에 있는 perm도 함께 바뀐다.
        methods.append(perm[:])
        return
    else:
        for i in range(0, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                perm.append(i)
                sharkMovePermutations(nx, ny, perm, remain - 1)
                perm.pop()


# 물고기 한 마리가 이동
def fishMove(fish, shark, smell):
    x = fish[0]
    y = fish[1]
    d = fish[2]

    # 45도 반시계 회전
    for i in range(d, d - 8, -1):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if shark[0] == nx and shark[1] == ny:
                continue
            if smell[nx][ny] > 0:
                continue
            if i < 0:
                d = 8 + i
            else:
                d = i
            return nx, ny, d
    return x, y, d


def sharkMove(shark, method):
    x = shark[0]
    y = shark[1]

    for direct in method:
        x += dx[direct]
        y += dy[direct]

    return [x, y]


forPrint = ["⬅️", "↖️", "⬆️", "↗️", "➡️", "↘️", "⬇️", "↙️"]


def printStatus(fishes, shark):
    grid = [[[] for __ in range(n)] for _ in range(n)]
    for fi, fish in fishes.items():
        x, y, d = fish
        grid[x][y].append(forPrint[d])
    grid[shark[0]][shark[1]] = "🦈"

    for g in grid:
        print(g)
    print()


def solution():
    global methods
    m, s = map(int, input().split())
    grid = [[[] for __ in range(n)] for _ in range(n)]  # grid[i][j] = [...] = i행 j열에 위치한 물고기들의 인덱스 리스트
    fishes = dict()  # fishes[i] = [xi, yi, di] = i 번째 물고기의 위치와 방향

    for i in range(m):
        x, y, d = map(int, input().split())
        fishes[i] = [x - 1, y - 1, d - 1]
        # grid[x-1][y-1].append(i)
    shark = list(map(int, input().split()))
    shark[0] -= 1
    shark[1] -= 1

    smell = [[0] * n for _ in range(n)]  # 물고기 유효기간. smell[i][j] = n => n번째 턴 뒤 없어지는 냄새

    nextFishIndex = max(fishes) + 1  # fishes에서 out시키면 del 시키므로, 다음 fish 인덱스를 저장한다.

    for turn in range(s):
        # 1. 물고기 복제
        copiedFishes = []
        for fish in fishes.values():
            copiedFishes.append(fish)

        # printStatus(fishes, shark)

        # 2. 물고기 이동
        grid = [[[] for __ in range(n)] for _ in range(n)]
        for fi, fish in fishes.items():
            x, y, d = fishMove(fish, shark, smell)
            fishes[fi] = [x, y, d]
            grid[x][y].append(fi)

        # printStatus(fishes, shark)

        # 3. 상어 이동
        methods = []
        sharkMovePermutations(shark[0], shark[1], [], 3)

        maxOutFishes = []  # 물고기의 인덱스 리스트
        maxOutFishesNum = -1
        maxMethod = []

        for method in methods:
            fishesOnMethod = countFish(shark, method, grid) # 물고기의 인덱스 리스트
            if (len(fishesOnMethod) > maxOutFishesNum) \
                    or (len(fishesOnMethod) == maxOutFishesNum and dictionaryFirst(method, maxMethod)):
                maxOutFishes = fishesOnMethod
                maxOutFishesNum = len(fishesOnMethod)
                maxMethod = method

        # 3-1. 상어 이동
        shark = sharkMove(shark, maxMethod)

        # printStatus(fishes, shark)

        # 3-2. 물고기 제외 및 냄새 남기기
        # 이 때 4번에서 물고기 냄새가 옅어지므로 3으로 세팅한다.
        for fi in maxOutFishes:
            smell[fishes[fi][0]][fishes[fi][1]] = 3
            del fishes[fi]

        # 4. 물고기 냄새가 옅어진다.
        smell = smellGone(smell)

        # 5. 복제 마법 완료
        for copiedFish in copiedFishes:
            fishes[nextFishIndex] = copiedFish
            nextFishIndex += 1

        # printStatus(fishes, shark)

    return len(fishes)

if __name__ == '__main__':
    print(solution())