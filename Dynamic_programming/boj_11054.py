# 가장 긴 바이토닉 부분 수열
'''
참고 : https://pacific-ocean.tistory.com/158
참고 : https://suri78.tistory.com/7
i번째 값이 포함되는 바이토닉 수열의 최대길이 =
    i번째 값이 포함되는 증가 수열 최대 길이
    + i번째 값이 포함되는 감소 수열 최대 길이(= 뒤에서 부터 증가 수열 최대 길이)
    - 1(자기 자신 중복)
'''
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
dpI = [1 for _ in range(N)] # dp Increase
dpD = [1 for _ in range(N)] # dp Decrease
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dpI[i] = max(dpI[j] + 1, dpI[i])

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            dpD[i] = max(dpD[j] + 1, dpD[i])

for i in range(N):
    dp[i] = dpI[i] + dpD[i] - 1

print(max(dp))