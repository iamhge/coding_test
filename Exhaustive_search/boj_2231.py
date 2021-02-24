# 분해합
# 내 코드
import sys

N = int(sys.stdin.readline().rstrip())
digit = len(str(N)) # 자릿수
result = 0

for n in range(10*digit - 9*(digit-1), N):
    # ex) 216
    # "216" -> ["2", "1", "6"] -> 2, 1, 6 -> [2, 1, 6]
    nList = list(map(int, list(str(n))))
    ntmp = n
    for i in nList:
        ntmp += i
    if ntmp == N:
        result = n
        break

print(result)

# 다른 사람 방식 (for문을 더 적개 돎. 시간복잡도 낮음.)
'''
import sys
def solve(n):
    _min = n - len(str(n)) * 9
    _min = 1 if _min < 1 else _min
    for i in range(_min, n):
        _sum = i
        _sum += sum(map(int, str(i))) # 더 간단한 방식
        if _sum == N:
            print(i)
            return
    print(0)

N = int(sys.stdin.readline())
solve(N)

'''