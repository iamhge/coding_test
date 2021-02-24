# 빠른 A+B
import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(x + y)