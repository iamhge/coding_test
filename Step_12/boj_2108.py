# 통계학
# N은 홀수
import sys

N = int(sys.stdin.readline().rstrip())
numList = [0] * (4000+4000+1) # numList의 index 0~4000은 양수와 0, 4001~8000은 음수(-4000~-1)를 나타냄

minNum = 4001
maxNum = -4001
allSum = 0
maxFrequency = 0

for _ in range(N):
    newNum = int(sys.stdin.readline().rstrip())
    numList[newNum] += 1
    # for range
    if newNum > maxNum:
        maxNum = newNum
    if newNum < minNum:
        minNum = newNum
    # for mean
    allSum += newNum
    # for mode
    if numList[newNum] > maxFrequency:
        maxFrequency = numList[newNum]
        mode = newNum

tmp = 1
if numList.count(maxFrequency) > 1:
    for i in range(minNum, maxNum+1):
        if numList[i] != maxFrequency: continue
        elif tmp != 0:
            tmp -= 1
            continue
        else:
            mode = i
            break

# for median
medianLoc = (N + 1)/2
for i in range(minNum, maxNum+1):
    while numList[i] != 0:
        medianLoc -= 1
        numList[i] -= 1
        if medianLoc == 0:
            median = i
            break

mean = allSum / N
maxRange = maxNum - minNum

print(round(mean))
print(median)
print(mode)
print(maxRange)