# 왕실의 나이트
import sys

xy = sys.stdin.readline().rstrip()
x = ord(xy[0]) - ord('a') + 1
y = int(xy[1])

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]
count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)

# 책 풀이 방식
'''
import sys

xy = sys.stdin.readline().rstrip()
x = ord(xy[0]) - ord('a') + 1
y = int(xy[1])

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
'''