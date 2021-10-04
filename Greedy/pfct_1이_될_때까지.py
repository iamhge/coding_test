# 1이 될 때까지
'''
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
'''

# 책 풀이 방식
import sys

N, K = map(int, sys.stdin.readline().split())
count = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 뺀다
    target = (N // K) * K
    count += N - target
    N = target
    
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if (N < K):
        break

    # K로 나누기
    count += 1
    N //= K

count += N - 1

print(count)