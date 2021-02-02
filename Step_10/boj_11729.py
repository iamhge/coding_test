import sys

def hanoi(n: int, start:int, temp:int, end:int):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, temp) 
        print(start, end)
        hanoi(n-1, temp, start, end)


n = int(sys.stdin.readline().rstrip())
K = 0

for i in range(n):
    K += 2**i

print(K)
hanoi(n, 1, 2, 3)

# 다른 사람 코드 (K 구하는 방법)
'''
K = 2 ** n - 1
'''