# 문자열 반복
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    S_temp = ''
    for c in S:
        S_temp += c*int(R)
    print(S_temp)