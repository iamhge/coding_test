# 내리막 길
'''
<아이디어>
  1. 그래프
      * visited 어떻게 처리할지 고민했는데, 생각해보니 왔던 길을 갈 일이 없음.
        (오로지 내리막길로만 가기 때문에 왔던 길은 갈 수 도 없음)
  2. Dynamic Programming + 그래프(재귀 이용)
      * (x, y)에 가는 경우의 수 = 상하좌우에서 (x, y)에 올 수 있는 경우의 수를 모두 합한 것.
      * (N-1, M-1)에서 (0, 0)으로 되돌아가며 탐색한다.
      * 이미 dp를 구한 노드는 다시 탐색할 필요가 없으므로, 상하좌우 탐색없이 그대로 반환한다.
  3. dp를 0이 아닌 -1로 초기화하는 이유 : https://www.acmicpc.net/board/view/49555
<틀린 이유>
  1. 시간 초과 (무한 루프)
     반례)
       input : https://gist.github.com/xdoju/4c848cf5c5a7295e0732c10b325107cc
       output : https://gist.github.com/xdoju/fd2fb61d007cca110c19e35e68d33217
  2. 런타임 에러
     sys.setrecursionlimit(10000) 추가 안해줘서
     참고) https://www.acmicpc.net/board/view/14844
<참고>
  백준 1520 내리막 길 (파이썬)
   : https://chldkato.tistory.com/114
'''
import sys
sys.setrecursionlimit(10000) # 이거 안넣으면 runtime error

dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]

def DFS(M, N, Map, x, y, dp): 
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]

        if (0 <= x_ < N) and (0 <= y_ < M): # 범위 체크  
            if Map[y_][x_] > Map[y][x]:
                dp[y][x] += DFS(M, N, Map, x_, y_, dp)

                # for k in range(M):
                #     print(dp[k])
                # print()

    return dp[y][x]

def main():
    M, N = map(int, sys.stdin.readline().split())
    Map = []
    for _ in range(M):
        Map.append(list(map(int, sys.stdin.readline().split())))
    
    dp = [[-1]*N for _ in range(M)]
    dp[0][0] = 1
    print(DFS(M, N, Map, N-1, M-1, dp))

if __name__=="__main__":
    main()

# 시간 초과
# pypy로 해도 시간초과 됨. 무한루프를 돎.
'''
import sys
from collections import deque

def solution(M: int, N: int, Map: list):
    stack = deque([(0, 0)])
    dx = [0, 0, -1, 1] # 상하좌우
    dy = [-1, 1, 0, 0]
    result = 0
    
    while stack:
        x, y = stack.pop()

        if x == N-1 and y == M-1:
            result += 1
            continue

        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if (0 <= x_ < N) and (0 <= y_ < M): # 범위 체크
                if Map[y_][x_] < Map[y][x]:
                    stack.append((x_, y_))

    return result

def main():
    M, N = map(int, sys.stdin.readline().split())
    Map = []
    for _ in range(M):
        Map.append(list(map(int, sys.stdin.readline().split())))

    print(solution(M, N, Map))

if __name__=="__main__":
    main()
'''