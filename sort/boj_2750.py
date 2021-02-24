# 수 정렬하기

# 방법 1
# 이게 더 오래걸림.
'''
import sys

N = int(sys.stdin.readline().rstrip())
numList = []

for _ in range(N):
    newNum = int(sys.stdin.readline().rstrip())

    if len(numList) == 0:
        numList.append(newNum)
    else:
        for i in range(0, len(numList)):
            if numList[i] > newNum:
                numList.insert(i, newNum)
                break
            if i == len(numList)-1:
                numList.append(newNum)

for num in numList:
    print(num)
'''

# 방법 2
import sys

N = int(sys.stdin.readline().rstrip())
numList = []
for _ in range(N):
    numList.append(int(sys.stdin.readline().rstrip()))

numList.sort()

for num in numList:
    print(num)