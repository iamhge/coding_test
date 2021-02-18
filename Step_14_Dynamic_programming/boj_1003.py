# 피보나치 함수
'''
N = 0인 경우 : 1 0 
N = 1인 경우 : 0 1
N = 2인 경우 : 1 2
N = 3인 경우 : 2 3
N = 4인 경우 : 3 5
N = 5인 경우 : 5 8
N = 6인 경우 : 8 13
N = 7인 경우 : 13 21
.
.
.
N = n인 경우
0이 출력되는 횟수는 n-1일 때 1이 출력되는 횟수
1이 출력되는 횟수는 n-1일 때 1이 출력되는 횟수 + 0이 출력되는 횟수
'''
import sys

def countZeroOneInFib(N: int):
    countZO = [0]*2

    if N == 0:
        countZO[0] = 1
        countZO[1] = 0
    else:
        countZOInN_1 = countZeroOneInFib(N-1)
        countZO[0] = countZOInN_1[1]
        countZO[1] = countZOInN_1[0] + countZOInN_1[1]

    return countZO

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    count = countZeroOneInFib(N)
    print(count[0], count[1])

# 다른 사람 코드
# 배열에 모두 담으면서 계산 (대부분 이 방법 사용함)
# 0이 출력되는 횟수 = f[i-2][0]+f[i-1][0] (n-2일 때 0이 출력되는 횟수 + n-1일 때 0이 출력되는 횟수)
# 1이 출력되는 횟수 = f[i-2][1]+f[i-1][1] (n-2일 때 1이 출력되는 횟수 + n-1일 때 1이 출력되는 횟수)
'''
from sys import stdin
T = int(input())
l = [int(stdin.readline()) for _ in range(T)]
f = [[1, 0], [0, 1]]
for i in range(2, max(l)+1):
    f.append([f[i-2][0]+f[i-1][0], f[i-2][1]+f[i-1][1]])

for i in l:
    print(' '.join(map(str, f[i])))
'''