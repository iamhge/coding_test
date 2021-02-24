# 최댓값
import sys

N = []
for _ in range(9):
    N.append(int(sys.stdin.readline().rstrip()))

m = max(N)
print(m, N.index(m)+1, sep='\n')