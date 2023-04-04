# 벽 부수고 이동하기
'''
<아이디어>
  1. 벽을 하나씩 뚫고 BFS를 진행하는 방식 -> 시간초과
  2. 1의 방법을 사용하되, BFS 재수행시 보다 최적인 경우에만 더 진행하고 아니면 멈추도록 -> 역시 시간초과
  3. <참고>를 참고하여, 1번의 BFS로 최단 거리를 구하도록 수정
     1) visited를 N*M*2크기의 3차원 list로 만들어 벽을 뚫었는지의 여부를 저장한다.
        visited[x][y][w]에서 w가 1인 경우는 아직 벽을 뚫지 않은 경우, 0인 경우는 벽을 뚫은 경우이다.
     2) 벽이 아닌 경우 일반적인 BFS 수행
     3) 벽이고, 그 벽을 뚫은 적이 없는 경우 세번째 차수 값을 수정하여 큐에 삽입
     4) 결과적으로 한 번의 BFS 수행으로 벽을 한 개까지 부쉈을 때의 최단 거리를 구한다.
     * 벽을 한번 뚫은 경우와 벽을 뚫지 않은 경우들을 한번에 BFS탐색한다고 생각하면 됨.
<기억할 것>
  1. 이렇게 상태(벽을 뚫었는가, 뚫지 않았는가)를 기반으로 한 경우의 문제는
     해당 상태를 저장하고 문제를 푸는 방법을 활용하자.
  2. BFS는 너비탐색이므로, 벽을 뚫었건 뚫지 않았건 최적은 먼저 도착하게 되어있다는 점 명심.
<틀린 이유> 
  * 시간 초과
<참고>
  백준 2206 벽 부수고 이동하기 (파이썬)
   : https://chldkato.tistory.com/19
  [백준] 2206번(python 파이썬)
   : https://pacific-ocean.tistory.com/348
'''
import sys
from collections import deque

def BFS(N: int, M: int, Map: list):
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)]
    queue = deque([(0, 0, 1)])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[0][0][1] = 1

    while queue:
        x, y, w = queue.popleft()
        # for i in range(N):
        #     print(visited[i])
        # print()

        if x == M-1 and y == N-1:
            return visited[y][x][w]
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < M and 0 <= y_ < N:
                # 벽이 없고, w 상태에서 방문한 적이 없는 경우.
                if Map[y_][x_] == 0 and visited[y_][x_][w] == 0:
                    visited[y_][x_][w] = visited[y][x][w] + 1
                    queue.append((x_, y_, w))
                # 벽이 있고, 벽을 뚫을 수 있는 상태인 경우(이전에 뚫은 적이 없는 경우).
                elif Map[y_][x_] == 1 and w == 1:
                    visited[y_][x_][0] = visited[y][x][1] + 1
                    queue.append((x_, y_, 0))

    return -1

def main():
    N, M = map(int, sys.stdin.readline().split())
    Map = []
    for _ in range(N):
        Map.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
    print(BFS(N, M, Map))

if __name__=="__main__":
    main()