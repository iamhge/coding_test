# 미래 도시
'''
ex1)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

ex2)
4 2
1 3
2 4
3 4
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

def printGraph():
    for i in range(N+1):
        print(graph[i])
    print()


for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
X, K = map(int, input().split())

for i in range(1, N+1):
    graph[i][i] = 0
    
for now in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = graph[b][a] = min(graph[a][b], graph[a][now] + graph[now][b])

cost = graph[1][K] + graph[K][X]

if cost >= INF:
    print(-1)
else:
    print(cost)