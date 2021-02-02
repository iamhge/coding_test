import sys

N = int(sys.stdin.readline().rstrip())

if N % 5 == 0:
    result = N // 5
else:
    result = -1
    for i in range(N // 5, 0, -1):
        if (N - 5*i) % 3 == 0:
            result = i + (N - 5*i) // 3
            break
    if (result == -1) and (N % 3 == 0):
        result = N // 3

print(result)