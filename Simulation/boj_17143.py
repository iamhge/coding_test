# 낚시왕
'''
<풀이 방법>
  - 이동 후 좌표 값?
  - n-1 만큼 나눈 몫이 (n은 해당 열 혹은 행의 길이)
    1) 짝수일 경우
        -> 방향 그대로
    2) 홀수일 경우
        -> 방향 변경
    3) 최종 좌표
        3-1) nx 를 2*(n-1)로 나눈 나머지 값을 구한다.
             -> nx %= 2*(n - 1)
        3-2) 3-1의 값이 n-1보다 크다면, n-1번째 인덱스에서 줄어드는 방향이고,
             n-1보다 작다면 0번째 인덱스에서 커지는 방향이다.
        3-3) 따라서 3-1의 값이 n-1보다 크다면
             -> nx = (n - 1) - (nx - (n - 1)) = 2*(n - 1) - nx
             3-1의 값이 n-1보다 작다면
             -> nx = 0 + nx = nx
'''

# 상 하 우 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
changeDirect = [1, 0, 3, 2]


def fishing(king, sea, sharkInfoList, dead, gotcha):
    for s in sea:
        if s[king] != -1:
            gotcha.append(sharkInfoList[s[king]][-1])
            dead.append(s[king])
            break
    return dead, gotcha


def sharkSurvive(sharkInfoList, sharkInfo, i, sea, dead):
    # 다른 상어가 없을 경우
    if sea[sharkInfo[0]][sharkInfo[1]] == -1:
        sea[sharkInfo[0]][sharkInfo[1]] = i
    # 다른 상어가 있는 경우
    else:
        anotherSharkInfo = sharkInfoList[sea[sharkInfo[0]][sharkInfo[1]]]
        # 다른 상어보다 큰 경우
        if anotherSharkInfo[-1] < sharkInfo[-1]:
            dead.append(sea[sharkInfo[0]][sharkInfo[1]])
            sea[sharkInfo[0]][sharkInfo[1]] = i
        # 다른 상어가 더 큰 경우
        else:
            dead.append(i)

    return sea, dead


def sharkMove(R, C, sharkInfo):
    nx = sharkInfo[0] + dx[sharkInfo[3]] * sharkInfo[2]
    ny = sharkInfo[1] + dy[sharkInfo[3]] * sharkInfo[2]

    # 상 하
    if sharkInfo[3] < 2:
        # 방향 변경
        if (nx // (R - 1)) % 2 != 0:
            sharkInfo[3] = changeDirect[sharkInfo[3]]

        nx %= 2*(R - 1)
        nx = abs(nx)
        if nx > R-1:
            nx = 2*(R - 1) - nx
    # 우 좌
    else:
        # 방향 변경
        if (ny // (C - 1)) % 2 != 0:
            sharkInfo[3] = changeDirect[sharkInfo[3]]

        ny %= 2 * (C - 1)
        ny = abs(ny)
        if ny > C - 1:
            ny = 2 * (C - 1) - ny

    sharkInfo[0] = nx
    sharkInfo[1] = ny

    return sharkInfo


def main():
    R, C, M = map(int, input().split())
    dead = []  # 죽거나 잡힌 상어의 index 기록
    gotcha = []  # 잡힌 상어의 크기

    # r, c, s, d, z
    # (r,c) = 위치
    # s = 속력
    # d = 이동방향 (1~4 -> 상 하 우 좌)
    # z = 크기
    sharkInfoList = []
    sea = [[-1] * C for _ in range(R)]  # 상어의 index를 표시한다.

    for i in range(M):
        sharkInfo = list(map(int, input().split()))
        sharkInfo[0] -= 1
        sharkInfo[1] -= 1
        sharkInfo[3] -= 1
        sharkInfoList.append(sharkInfo)
        sea[sharkInfo[0]][sharkInfo[1]] = i

    for i in range(C):
        # 낚시
        dead, gotcha = fishing(i, sea, sharkInfoList, dead, gotcha)

        # 상어 이동
        sea = [[-1] * C for _ in range(R)]
        for si, sharkInfo in enumerate(sharkInfoList):
            if si in dead:
                continue
            sharkInfo = sharkMove(R, C, sharkInfo)
            sea, dead = sharkSurvive(sharkInfoList, sharkInfo, si, sea, dead)

        # for s in sea:
        #     print(s)
        # print()

    print(sum(gotcha))

main()