# 1이 될 때까지
import sys

N, K = map(int, sys.stdin.readline().split())
count = 0

while (N >= K):
    if (N % K != 0):
        count += N % K
        N -= N % K
        
    while (N % K == 0):
        count += 1
        N //= K

count += N - 1

print(count)