# N-Queen
'''
<풀이 방법>
  - N개의 퀸이 서로를 공격할 수 없도록 배치하면, 각 퀸은 서로 다른 행과 열에 위치한다.
  - 1번째 행에서 부터 N번째 행까지 퀸을 배치할 때, ak번째 퀸의 위치는 ak-1까지의 퀸의 대각선, 아래가 아닌 곳에 위치한다.
  - 백트래킹 + 브루트 포스
    - 1번째 -> N번째 행까지 탐색하다가 답이 아니면 탐색을 stop한다.
    - visitedCol[i] = i번째 열에 있는 퀸의 행
    - abs(r - visitedCol[j]) == abs(j - i) -> i번째 열이 j번째 열의 퀸의 대각선에 위치하는 경우
'''
def DFS(n, r, c, vCol):
    result = 0
    visitedCol = vCol[:]
    visitedCol[c] = r
    
    if r == n-1:
        return 1
    
    for i in range(n):
        if visitedCol[i] != -1: continue
        if c-1 <= i <= c+1: continue
        for j in range(n):
            if visitedCol[j] == -1: continue
            if abs(r+1 - visitedCol[j]) == abs(i - j):
                break
        else:
            result += DFS(n, r+1, i, visitedCol)
    return result

def solution(n):
    answer = 0
    for i in range(n):
        answer += DFS(n, 0, i, [-1 for _ in range(n)])
    return answer