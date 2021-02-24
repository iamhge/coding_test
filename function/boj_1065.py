# 한수
import sys

# 한수 여부 return
def arithmeticSequence(num:int) -> bool:
    if num < 100:
        return True

    strNum = str(num)
    diff = int(strNum[0]) - int(strNum[1])

    for i in range(1, len(strNum)):
        if (int(strNum[i-1]) - int(strNum[i]) != diff):
            return False
            
    return True

N = int(sys.stdin.readline().rstrip())
asNum = 0
for i in range(1, N+1):
    if arithmeticSequence(i):
        asNum += 1
print(asNum)