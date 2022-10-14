# 연구소 3
'''
pypy3으로 제출해서 정답...
'''
from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
seqs = []


def bfs(active):
    queue = deque([])
    maxSeq = 0
    visited = [[False] * n for _ in range(n)]

    for x, y in active:
        queue.append((x, y, 0))
        visited[x][y] = True

    while queue:
        x, y, seq = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] or lab[nx][ny] == 1:
                    continue
                if lab[nx][ny] == 0 and maxSeq < seq + 1:
                    maxSeq = seq + 1
                queue.append((nx, ny, seq + 1))
                visited[nx][ny] = True

    if sum(visited, []).count(False) == walls:
        seqs.append(maxSeq)

    return


def combinations(start, combi, m):
    global n, viruses
    if m == 0:
        bfs(combi)
    else:
        for i in range(start, len(viruses)):
            combi.append(viruses[i])
            combinations(i+1, combi, m-1)
            combi.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    lab = []
    viruses = []
    walls = 0

    for i in range(n):
        lab.append(list(map(int, input().split())))
        for j in range(n):
            if lab[i][j] == 2:
                viruses.append((i, j))
            if lab[i][j] == 1:
                walls += 1

    for i in range(len(viruses)):
        combinations(i, [], m)

    if len(seqs) == 0:
        print(-1)
    else:
        print(min(seqs))