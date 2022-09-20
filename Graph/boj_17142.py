# 연구소 3
'''
<오답 노트>
  - 이전 코드들에 
    ```
    if sequence[x][y] < seq:
            continue
        sequence[x][y] = seq
    ```
    위 코드 넣었던 이유가 여러개 겹치면서 더 최선의 seq가 나올까봐 였는데
    생각해보면 BFS라서 겹치지 않게 코드 짤 수 있다.
  - 시간 초과 때문에 다른 사람 코드 참고
<참고>
  - [백준] #17142 - 연구소 3 (파이썬, Python)
    https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-17142-%EC%97%B0%EA%B5%AC%EC%86%8C-3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
<소감>
  - 아니 복잡도 그리 많이 차이 안날것같은데 억울해 죽겠어 ㅠㅠ
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열

def BFS(N, lab, root, sequence, wall):
    queue = deque(root)
    result = 0
    while queue:
        x, y, seq = queue.popleft()

        if sequence[x][y] != -1:
            continue
        if lab[x][y] != '2':
            result = seq
        sequence[x][y] = seq

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != '1':
                    
                    queue.append((nx, ny, seq + 1))
        # for s in sequence:
        #     print(s)
        # print()
    # print(list(sum(sequence, [])).count(-1))
    return result, (list(sum(sequence, [])).count(-1) == wall)

def solution(N, M, lab):
    answer = []
    virus = []
    wall = 0

    for i in range(N):
        for j in range(N):
            if lab[i][j] == '2':
                virus.append((i, j))
            if lab[i][j] == '1':
                wall += 1
    
    cases = list(combinations(virus, M))

    for case in cases:
        sequence = [[-1] * N for _ in range(N)]
        root = []
        for c in case:
            root.append((c[0], c[1], 0))
        seq, possible = BFS(N, lab, root, sequence, wall)
        # print(seq, possible)
        # for s in sequence:
        #     print(s)
        # print()
        if possible:
            answer.append(seq)
        
    if answer == []: return -1 
    return min(answer)

def main():
    N, M = map(int, input().split())
    lab = []

    for _ in range(N):
        lab.append(input().split())

    print(solution(N, M, lab))

main()

# 시간 초과
'''
import sys
from collections import deque, defaultdict
from itertools import combinations

input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열

def BFS(N, lab, root, sequence):
    queue = deque([root])

    while queue:
        x, y, seq = queue.popleft()

        if sequence[x][y] < seq:
            continue
        sequence[x][y] = seq

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != '1' and lab[nx][ny] != '2':
                    queue.append((nx, ny, seq + 1))

    return sequence

def solution(N, M, lab):
    answer = []
    virus = []

    for i in range(N):
        for j in range(N):
            if lab[i][j] == '2':
                virus.append((i, j))
    
    sequences = defaultdict(list)

    for v in virus:
        sequences[v] = BFS(N, lab, (v[0], v[1], 0), [[N*N+1] * N for _ in range(N)])

    cases = list(combinations(virus, M))

    for case in cases:
        total = 0  
        possible = True
        nowSequence = [[N*N+1] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if lab[i][j] == '1' or lab[i][j] == '2':
                    nowSequence[i][j] = -1
                    continue

                nowSequence[i][j] = min(sequences[c][i][j] for c in case)

                if lab[i][j] == '0' and nowSequence[i][j] >= N*N+1:
                    possible = False
                    break
            if not possible: break
            total = max(total, max(nowSequence[i]))
        
        if possible:
            answer.append(total)
        
    if answer == []: return -1 
    return min(answer)

def main():
    N, M = map(int, input().split())
    lab = []

    for _ in range(N):
        lab.append(input().split())

    print(solution(N, M, lab))

main()
'''
# 시간 초과
'''
<풀이 방법>
  - BFS
'''
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열

def BFS(N, lab, root, sequence):
    queue = deque(root)

    while queue:
        x, y, seq = queue.popleft()

        if sequence[x][y] < seq:
            continue
        sequence[x][y] = seq

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != '1' and lab[nx][ny] != '2':
                    queue.append((nx, ny, seq + 1))

    return sequence

def solution(N, M, lab):
    answer = []
    virus = []

    for i in range(N):
        for j in range(N):
            if lab[i][j] == '2':
                virus.append((i, j))
    
    cases = list(combinations(virus, M))

    for case in cases:
        total = 0
        possible = True
        sequence = [[N*N+1] * N for _ in range(N)]
        root = []
        for c in case:
            root.append((c[0], c[1], 0))
        sequence = BFS(N, lab, root, sequence)
        
        # sequence 검사
        for i in range(N):
            for j in range(N):
                if lab[i][j] == '1' or lab[i][j] == '2':
                    sequence[i][j] = -1
                if lab[i][j] == '0' and sequence[i][j] >= N*N+1:
                    possible = False
                    break
            if not possible: break
            total = max(total, max(sequence[i]))
        
        if possible:
            answer.append(total)
        
    if answer == []: return -1 
    return min(answer)

def main():
    N, M = map(int, input().split())
    lab = []

    for _ in range(N):
        lab.append(input().split())

    print(solution(N, M, lab))

main()
'''