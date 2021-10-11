# 위에서 아래로
import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = [0 for i in range(N)]
for i in range(N):
    nums[i] = int(input().rstrip())

nums.sort(reverse=True)

for num in nums:
    print(num, end=' ')