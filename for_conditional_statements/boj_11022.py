# A+B - 8
import sys
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d ="%(i+1,a,b), a+b)