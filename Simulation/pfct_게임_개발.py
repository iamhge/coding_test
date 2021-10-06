# 게임 개발
import sys

N, M = map(int, sys.stdin.readline().split())
A, B, d = map(int, sys.stdin.readline().split())
Map = []
for i in range(N):
    Map.append(list(map(int, sys.stdin.readline().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

while Map[A][B] != 1:
    # 지나간 자리 표시
    if Map[A][B] == 0:
        Map[A][B] = 2
        count += 1

    # 회전
    for _ in range(4):
        # 왼쪽으로 회전
        d -= 1
        if d < 0:
            d += 4
        nx = A + dx[d]
        ny = B + dy[d]

        # 가보지 않은 칸이면 이동
        if Map[nx][ny] == 0:
            A, B = nx, ny
            break

    # 회전하는 동안 이동이 없었으면 뒤로 이동
    if A != nx or B != ny:
        A -= dx[d]
        B -= dy[d]

print(count)