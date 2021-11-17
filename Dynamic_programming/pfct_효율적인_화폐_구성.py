# 효율적인 화폐 구성
'''
a_n = n원을 만들기 위한 최소한의 화폐 개수
a_n = min( a_n-money[0], a_n-money[1], ... , a_n-money[N-1] ) + 1
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
money = [0] * N

for i in range(N):
    money[i] = int(input().rstrip())

d = [10001] * (M + 1)

for m in money:
    if m < M:
        d[m] = 1

for i in range(min(money), M+1):
    for j in range(N):
        d[i] = min(d[i - money[j]] + 1, d[i])

if d[M] == 10001:
    print(-1)
else:
    print(d[M])