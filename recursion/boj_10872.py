import sys

def factorial(N: int):
    if N <= 1:
        return 1
    return N * factorial(N-1)

N = int(sys.stdin.readline().rstrip())
print(factorial(N))