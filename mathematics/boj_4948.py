# 베르트랑 공준
import sys

def getPrimeNumber(M: int, N: int):
    isPrime = [True] * (N + 1)
    isPrime[1] = False
    Prime = []

    for i in range(2, int(N**0.5) + 1): 
        if isPrime[i]:
            for j in range(2*i, N+1, i):
                isPrime[j] = False

    for i in range(M, N+1):
        if isPrime[i]:
            Prime.append(i)
            
    return Prime

while True:
    n = int(sys.stdin.readline().rstrip())
    if not n:
        break
    print(len(getPrimeNumber(n + 1, 2*n)))