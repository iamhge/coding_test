# 나무 재테크
'''
- 계속 시간 초과 났으나, pypy3으로 시간 초과 면함...
'''

global n
global tree
global food
global a

# 인접한 칸
rClose = [-1, -1, -1, 0, 0, 1, 1, 1]
cClose = [-1, 0, 1, -1, 1, -1, 0, 1]


def year():
    global tree, food, a
    breed = []
    for i in range(n):
        for j in range(n):
            if not tree[i][j]:
                # --- Winter ---
                food[i][j] += a[i][j]
                continue
            # --- Spring ---
            survive = []
            newFood = 0
            for l in range(len(tree[i][j]) - 1, -1, -1):
                t = tree[i][j][l]
                # 양분 부여
                if food[i][j] - t >= 0:
                    food[i][j] -= t
                    survive.append(t + 1)
                    if (t + 1) % 5 == 0:
                        breed.append([i, j])
                # 남은 나무들이 더 이상 양분을 못 먹게 되면
                else:
                    newFood += t // 2

            tree[i][j] = survive[::-1]
            # --- Summer & Winter ---
            food[i][j] += newFood + a[i][j]

    # --- Fall ---
    for r, c in breed:
        for k in range(8):
            nr = r + rClose[k]
            nc = c + cClose[k]
            if 0 <= nr < n and 0 <= nc < n:
                tree[nr][nc].append(1)


def printTF():
    global tree, food
    print("--- Tree ---")
    for t in tree:
        print(t)
    print()
    print("--- Food ---")
    for f in food:
        print(f)
    print()


def main():
    global n, tree, food, a
    answer = 0
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    tree = [[[] for __ in range(n)] for _ in range(n)]
    for i in range(m):
        x, y, z = map(int, input().split())
        tree[x - 1][y - 1].append(z)

    food = [[5] * n for _ in range(n)]

    for i in range(k):
        year()

    for i in range(n):
        for j in range(n):
            answer += len(tree[i][j])

    return answer


print(main())

# 시간 초과
'''
global n
global tree
global food
global a

# 인접한 칸
rClose = [-1, -1, -1, 0, 0, 1, 1, 1]
cClose = [-1, 0, 1, -1, 1, -1, 0, 1]


def springSummer():
    global tree, food
    for i in range(n):
        for j in range(n):
            # 나무가 있으면
            if len(tree[i][j]) > 0:
                newTrees = []
                newFood = 0
                for t in tree[i][j]:
                    # 양분 부여
                    if food[i][j] - t >= 0:
                        food[i][j] -= t
                        newTrees.append(t + 1)
                    # 남은 나무들이 더 이상 양분을 못 먹게 되면
                    else:
                        newFood += t / 2
                tree[i][j] = newTrees
                food[i][j] += newFood


def fallWinter():
    global n, tree, food, a
    for i in range(n):
        for j in range(n):
            for t in tree[i][j]:
                if t % 5 == 0:
                    for k in range(8):
                        nr = i + rClose[k]
                        nc = j + cClose[k]
                        if 0 <= nr < n and 0 <= nc < n:
                            tree[nr][nc].insert(0, 1)
            food[i][j] += a[i][j]

def printTF():
    global tree, food
    print("--- Tree ---")
    for t in tree:
        print(t)
    print()
    print("--- Food ---")
    for f in food:
        print(f)
    print()

def main():
    global n, tree, food, a
    answer = 0
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    tree = [[[] for __ in range(n)] for _ in range(n)]
    for i in range(m):
        x, y, z = map(int, input().split())
        tree[x - 1][y - 1].append(z)

    # 어린 나무 부터 양분을 주기 위해 정렬
    for i in range(n):
        for j in range(n):
            tree[i][j].sort()

    food = [[5] * n for _ in range(n)]

    for i in range(k):
        springSummer()
        fallWinter()

    for i in range(n):
        for j in range(n):
            answer += len(tree[i][j])

    return answer

print(main())
'''
