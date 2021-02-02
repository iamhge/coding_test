import sys
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d:"%(i+1), a+b)