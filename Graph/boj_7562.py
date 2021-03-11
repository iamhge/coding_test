# 나이트의 이동
'''
<아이디어>
  * 단순한 BFS. 그저 퍼지는 좌표가 변형되었을 뿐이다.
<틀린 이유>
  * queue.append((x_, y_))를 queue.append((y_, x_))라고 함.
  * return visited[end[1]][end[0]]를 return visited[end[0]][end[1]]라고 함.
'''
import sys
from collections import deque

input = sys.stdin.readline

def BFS(I: int, root: tuple, end: tuple):
    visited = [[0]*I for _ in range(I)]
    dx = [1, 2, 2, 1, -1, -2, -2, -1] # 시계 방향
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    queue = deque([root])

    while queue:
        x, y = queue.popleft()

        if x == end[0] and y == end[1]:
            break

        for i in range(8):
            x_ = x + dx[i]
            y_ = y + dy[i]

            if 0 <= x_ < I and 0 <= y_ < I:
                if visited[y_][x_] == 0:
                    queue.append((x_, y_))
                    visited[y_][x_] = visited[y][x] + 1
        
    return visited[end[1]][end[0]]

def main():
    T = int(input().rstrip())

    for _ in range(T):
        I = int(input().rstrip())
        sx, sy = map(int, input().split())
        ex, ey = map(int, input().split())

        print(BFS(I, (sx, sy), (ex, ey)))

if __name__=="__main__":
    main()