# 텀 프로젝트
'''
<아이디어>
  * 탐색의 처음(root)과 끝이 같아야 한 팀이 될 수 있음.
  * S[i] : i번째 학생이 선택한 학생의 번호
<틀린 이유>
  * 시간 초과 
    -> pypy로 해도 계속 79퍼에서 시간초과 
    -> 기존에는 사이클 형성 부분을 순회하며 0으로 setting해서 사이클을 다시 순회하지 않는 방식.
    -> 집합으로 바꿨으나 또 시간초과
    -> 돌다가 이미 팀을 이룬 학생을 고른 경우 break처리
    -> 그래도 시간초과
    -> 별 난리를 쳐도 다 시간초과. 구글링 해도 나랑 비슷한데 왜 난 시간초과 인지 모르겠음.. -> 포기
'''
import sys
from collections import deque

def DFS(S: list, root: int, cycle: set, visited: list):
    picked = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n in visited:
            break

        visited.append(n)
        picked.append(n)

        if S[n] not in picked:
            stack.append(S[n])
        else: # 사이클이 이뤄졌을 때
            cycle |= set(picked[picked.index(S[n]):])
            break

    return S, cycle, visited

def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        S = [0]
        cycle = set()
        visited = []
        S.extend(list(map(int, sys.stdin.readline().split())))

        for i in range(1, n+1):
            if i not in visited:
                S, cycle, visited = DFS(S, i, cycle, visited)
                
        print(n - len(cycle))
        
if __name__=="__main__":
    main()