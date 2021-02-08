# 수 정렬하기 2
# 파이썬은 다 되지
import sys

N = int(sys.stdin.readline().rstrip())
numList = []
for _ in range(N):
    numList.append(int(sys.stdin.readline().rstrip()))

numList.sort()

for num in numList:
    print(num)