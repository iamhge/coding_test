# 여행경로
'''
<풀이 방법>
  - 백트래킹 (Backtracking)
  - DFS로 모든 노드를 순회할 수 있는지 검사한다.
'''
from collections import deque

def findNextTickets(now, tickets):
    for ticket in tickets:
        if ticket[0] == now:
            yield ticket

def DFS(tickets):
    visited = {tuple(ticket): 0 for ticket in tickets}
    for ticket in tickets:
        visited[tuple(ticket)] += 1
        
    stack = deque([( ["ICN"], visited.copy())])
    result = []
    
    while stack:
        route, remainTickets = stack.pop()
        if len(route) == len(tickets) + 1:
            result.append(route)
        for nextTicket in findNextTickets(route[-1], tickets):
            if remainTickets[tuple(nextTicket)] > 0:
                tmp = route[:]
                tmp.append(nextTicket[1])
                tmpRT = remainTickets.copy()
                tmpRT[tuple(nextTicket)] -= 1
                stack.append((tmp, tmpRT))
                
    return result

def solution(tickets):
    answer = DFS(sorted(tickets, key = lambda x: x[1]))
    if answer == []: return []
    return sorted(answer)[0]

# 다른 사람 풀이 1
'''
<풀이 방법>
  - 백트래킹 (Backtracking)
  - stack을 사용해서 풀이
'''
def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        # routes에 top이 없을 때 = 해당 위치에서 다른 곳으로 가는 티켓이 없을 때
        # routes[top]의 길이가 0일 때 = 다음에 갈 길이 없을 때
        # -> 결론적으로 끝에 당도했을 때
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1]) # routes에서 pop한 것을 stack에 넣는다. 다음 경로를 stack에 넣는다.
            routes[top] = routes[top][:-1] # routes의 끝을 자른다. (pop한다)
    return path[::-1]

# 다른 사람 풀이 2
'''
<개념>
  - defaultdict({type})
    : type을 기본값으로 dictionary를 생성한다.
    참고 : https://00h0.tistory.com/24
<풀이 방법>
  - 백트래킹 (Backtracking)
  - recursion
'''
from collections import defaultdict 

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    # key 공항에서 갈 수 있는 공항 순회
    for idx, country in enumerate(graph[key]):
        # 들어왔으니 graph에서 pop
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        # idx위치는 원래 country가 있던 곳. 
        # 즉, country 공항에 대해 dfs를 돌리고 key에서 갈 수 있는 다른 공항을 순회하기 위함.
        graph[key].insert(idx, country)

        # ret에 값이 존재한다는 것은, ret가 끝까지 가서 dfs 함수 상단의 if문에 걸렸다는 것을 의미하므로 return한다.
        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        # 알파벳 최상위 순서를 출력해야 하므로 sort한다.
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer