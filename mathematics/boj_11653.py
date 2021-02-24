# 소인수분해
# 내 코드
import sys

N = int(sys.stdin.readline().rstrip())
i = 2

while N >= 2:
    if N % i == 0:
        print(i)
        N /= i
        # i = 2 # <- 이거 해서 더 오래걸린듯
    else:
        i += 1

# 다른 사람 코드
'''
n = int(input())
for i in range(2, int(n**0.5)+1):
    while n % i == 0: # 안 나누어 떨어질 때까지 계속 반복
        n = n // i
        print(i)
if n > 1:
    print(n)
'''