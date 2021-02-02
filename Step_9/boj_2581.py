import sys
import math

def isPrimeNumber(num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True   

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
min = N + 1
sum = 0

for num in range(M, N + 1):
    if isPrimeNumber(num):
        sum += num
        if min > num:
            min = num

if sum == 0:
    print("-1")
else:
    print(sum)
    print(min)