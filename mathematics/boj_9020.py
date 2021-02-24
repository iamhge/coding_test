import sys

def isPrimeNumber(num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    for i in range(n//2, 0, -1):
        if isPrimeNumber(i) and isPrimeNumber(n-i):
            print(i, n-i)
            break