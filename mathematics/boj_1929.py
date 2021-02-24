# 내 코드 (좀 더 오래 걸림)
'''
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

M, N = map(int, sys.stdin.readline().split())

for num in range(M, N + 1):
    if isPrimeNumber(num):
        print(num)
'''

# 다른 사람 코드 (Top 100안 사람들 대부분 이 방식으로 풂)
M,N = map(int,input().split())

def get_prime(M,N):
    prime = [True] * (N+1)
    prime[1] = False
    for i in range(2,int(N ** 0.5)+1):
        if prime[i]:
            for j in range(i*2,N+1,i): # i의 배수들을 모두 제외시킴
                prime[j] = False
    return [i for i in range(M,N+1) if prime[i]]

for i in get_prime(M,N):
    print(i)
