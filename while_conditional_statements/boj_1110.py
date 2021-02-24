import sys

i = 0
N = list(sys.stdin.readline().rstrip())

if len(N) == 1:
    N.append(N[0])
    N[0] = '0'

M = N[:]

while True:
    sum = str(int(M[0]) + int(M[1]))
    M[0] = M[1]
    M[1] = sum[len(sum)-1]
    i += 1
    if (N == M):
        break

print(i)