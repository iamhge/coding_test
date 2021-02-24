import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    apart = [[0]*(n+1) for _ in range(k+1)]
    apart[0] = list(range(0, n+1))

    for i in range(1, n+1):
        for j in range(1, k+1):
            apart[j][i] = apart[j-1][i] + apart[j][i-1]
    print(apart[k][n])
