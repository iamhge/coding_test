# 날짜 계산
import sys

E, S, M = map(int, sys.stdin.readline().split())
i = 0

while 1:
    year = 28*i + S
    if year%15 == E%15  and year%19 == M%19:
        print(year)
        break
    i += 1