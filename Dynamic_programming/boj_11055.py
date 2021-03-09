# 가장 큰 증가 부분 수열
import sys
import copy

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
dp = copy.deepcopy(A)

for i in range(N):
    for j in range(i, -1, -1):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])

print(max(dp))

# 다른 사람 코드
# arr라는 list에 따로 저장함으로써, 자신보다 작은 수를 슬라이싱을 통해 탐색함.
'''
import sys

N = int(sys.stdin.readline())
arr = [0] * 1001
sequence = list(map(int, sys.stdin.readline().split()))

for seq in sequence:
    arr[seq] = max(arr[:seq]) + seq

sys.stdout.write(str(max(arr)))
'''