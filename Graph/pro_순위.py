# 순위
'''
<풀이 방법>
  - 각 Player를 이긴 사람 수와 Player에게 진 사람 수를 구한다.
  - (Player를 이긴 사람 수) + (Player에게 진 사람 수) == n - 1 이 되면 player의 순위가 확정된다.
  - 각 Player를 이기거나 진 사람 수는 DFS를 통해 매번 구한다.
'''
from collections import deque

def howManyPlayers(n, me, wl): # wl = 승패
    stack = deque([])
    stack.append(me)
    players = 0
    visited = [False] * (n+1)
    visited[me] = True
    
    while stack:
        now = stack.pop()
        
        for player in wl[now]:
            if visited[player]: continue
            stack.append(player)
            visited[player] = True
            players += 1
            
    return players

def solution(n, results):
    answer = 0

    win = {i:set() for i in range(1, n+1)} # i에게 이긴 선수들 (앞 순위)
    lose = {i:set() for i in range(1, n+1)} # i에게 진 선수들 (뒷 순위)
    
    for result in results:
        win[result[1]].add(result[0])
        lose[result[0]].add(result[1])

    for i in range(1, n+1):
        # i를 이긴 사람들
        winners = howManyPlayers(n, i, win)
        # i에게 진 사람들
        losers = howManyPlayers(n, i, lose)
        
        if winners + losers == n-1:
            answer += 1
            
    return answer

# 다른 사람 풀이
'''
<풀이 방법>
  - 풀이 개념은 나와 같으나 방법이 다르다.
  - 내 풀이와 달리, 그냥 순서대로 player를 순회하여 이긴 사람과 진 사람을 update 해 준다.
'''
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer