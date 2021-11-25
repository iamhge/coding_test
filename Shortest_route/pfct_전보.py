# 전보
'''
<개념>
  다익스트라 알고리즘
  
<예시>
ex)
3 2 1
1 2 4
1 3 2
'''

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

dist = [INF] * (N+1)

q = []
heapq.heappush(q, (0, C))
dist[C] = 0

while q:
    cost, now = heapq.heappop(q)
    if cost > dist[now]:
        continue
    for i in graph[now]:
        c = i[1] + cost
        if c < dist[i[0]]:
            dist[i[0]] = c
            heapq.heappush(q, (c, i[0]))

count = 0
time = -1
for i in range(1, N+1):
    if dist[i] < INF and i != C:
        count += 1
        time = max(time, dist[i])

print(count, time)