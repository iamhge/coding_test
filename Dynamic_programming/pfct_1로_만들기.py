# 1로 만들기
'''
a1 = 0
a2 = a1 + 1 = 1
a3 = 1
a4 = a3 + 1 or a2 + 1 = 2
a5 = 1

...

an = min(a_n/2 + 1, a_n/3 + 1, a_n/5 + 1, a_n-1 + 1)
'''
import sys

input = sys.stdin.readline

X = int(input().rstrip())
a = [0] * 30001
a[1] = 0
a[2] = 1
a[3] = 1

for i in range(4, X+1):
    a[i] = a[i-1] + 1
    if i % 5 == 0:
        a[i] = min(a[i//5] + 1, a[i])
    if i % 3 == 0:
        a[i] = min(a[i//3] + 1, a[i])
    if i % 2 == 0:
        a[i] = min(a[i//2] + 1, a[i])
    
print(a[X])