# 부품 찾기
import sys
input = sys.stdin.readline

# Binary search를 이용한 풀이

def binarySearch(L: list, target: int, start: int, end: int):
    while start <= end:
        mid = (start + end) // 2

        if target == L[mid]:
            return True
        elif target < L[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False

N = int(input().rstrip())
parts = list(map(int, input().split()))
parts.sort()
M = int(input().rstrip())
checkList = list(map(int, input().split()))

for i in range(M):
    if binarySearch(parts, checkList[i], 0, N-1):
        print("yes", end=" ")
    else:
        print("no", end=" ")

# 계수 정렬을 이용한 풀이
'''
parts = [0] * 1000001

N = int(input().rstrip())
for i in list(map(int, input().split())):
    parts[i] += 1

M = int(input().rstrip())
checkList = list(map(int, input().split()))

for i in checkList:
    if parts[i] != 0:
        print("yes", end=" ")
    else:
        print("no", end=" ")
'''

# 집합을 이용한 풀이
'''
N = int(input().rstrip())
parts = set(map(int, input().split()))
parts.sort()
M = int(input().rstrip())
checkList = list(map(int, input().split()))

for i in checkList:
    if i in parts:
        print("yes", end=" ")
    else:
        print("no", end=" ")
'''