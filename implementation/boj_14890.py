# 경사로

def canGo(n, l, x, y, dx, dy, mymap):
    # 경사로가 끝나는 위치
    change = -1

    for i in range(n - 1):
        nx = x + dx
        ny = y + dy
        # 올라갈 때
        if mymap[x][y] + 1 == mymap[nx][ny]:
            if i - l < change:
                return False
            change = i
        # 내려갈 때
        elif mymap[x][y] - 1 == mymap[nx][ny]:
            if i + l >= n or i < change:
                return False
            change = i + l
        # 높이 차이가 1칸 이상일 때
        elif mymap[x][y] != mymap[nx][ny]:
            return False
        x = nx
        y = ny

    return True


def main():
    answer = 0
    n, l = map(int, input().split())
    mymap = []
    for _ in range(n):
        mymap.append(list(map(int, list(input().split()))))

    for i in range(n):
        if canGo(n, l, i, 0, 0, 1, mymap):
            answer += 1
        if canGo(n, l, 0, i, 1, 0, mymap):
            answer += 1
    return answer

print(main())
