# 상하좌우
'''
import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(str, sys.stdin.readline().split()))

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 1
y = 1

for m in M:
    if m == 'L':
        tmp = 0
    elif m == 'R':
        tmp = 1
    elif m == 'U':
        tmp = 2
    else:
        tmp = 3
        
    if 1 <= x + dx[tmp] <= N and 1 <= y + dy[tmp] <= N:
        x += dx[tmp]
        y += dy[tmp]

print(x, y)
'''

# 책 풀이 방식
import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(str, sys.stdin.readline().split()))

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x = 1
y = 1

for m in M:
    for i in range(len(move_types)):
        if m == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if 1 <= nx <= N and 1 <= ny <= N:
        x = nx
        y = ny

print(x, y)