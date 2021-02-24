# 최소, 최대
import sys

# 내 코드
'''
N = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().split()))
max = li[0]
min = li[0]

for i in range(N-1):
    if max < li[i+1]:
        max = li[i+1]
    elif min > li[i+1]:
        min = li[i+1]

print(min, max)
'''

# 다른 사람 코드
_, *arr = map(int, sys.stdin.read().split())
print(min(arr), max(arr))