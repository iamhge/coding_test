'''
<풀이 방법>
  - 소모, 최소 피로도의 크기 순으로는 구할 수 없다. 방법을 알 수 없었다.
  - dungeons 가 1이상 8 이하 이므로 그냥 완전탐색으로 구한다.
ex 1)
80, [[10, 10], [50, 10], [70, 20]] -> 3
'''
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    perms = list(permutations(dungeons))
    
    for perm in perms:
        tmpk = k
        canGo = 0
        for i in range(n):
            if tmpk >= perm[i][0]:
                tmpk -= perm[i][1]
                canGo += 1
        
        answer = max(answer, canGo)
        if answer == n:
            break
    
    return answer

# 다른 사람 풀이 1
'''
<풀이 방법>
  - 공식을 구해서 풂
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
'''
'''
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer
'''

# 다른 사람 풀이 2
'''
<풀이 방법>
  - DFS라고 명시하긴 했지만 사실상 재귀 함수를 이용한 완전 탐색으로 보임.
'''
'''
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
'''