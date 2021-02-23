# 주유소
'''
<아이디어>
  edge : 4 2 3 1
  vertex : 3-5-4-2-1 이라고 하면
  3-5-4-2-1까지 중에서 min of vertex는 2
  3-5-4-2, 3-5-4, 3-5, 3까지 중에서 min of vertex는 3
  so, 각 경우의 min of vertex만큼 각 경우의 끝의 edge에서 사야함.
  min :     3           3           3           2
            ↑           ↑           ↑           ↑
      3 ---(4)--- 5 ---(2)--- 4 ---(3)--- 2 ---(1)--- 1
  result = 2*1 + 3*3 + 3*2 + 3*4 = 29
  결론적으로는 첫번째 지역에서 9L를 사고, 네번째 지역에서 1L를 구매.
'''
import sys

N = int(sys.stdin.readline().rstrip())
edge = list(map(int, sys.stdin.readline().split()))
vertex = list(map(int, sys.stdin.readline().split()))
result = 0
minOfVertex = 1000000000

for i in range(N-1):
    if minOfVertex > vertex[i]:
        minOfVertex = vertex[i]
    result += minOfVertex*edge[i]

print(result)

# 시간 초과
'''
for i in range(N-1, 0, -1):
    result += edge[i-1] * min(vertex[:i])
'''