# ATM
import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))
P.sort()

for i in range(N-1):
    P[i+1] += P[i]

print(sum(P))