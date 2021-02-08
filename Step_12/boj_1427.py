# 소트인사이드
import sys

N = list(sys.stdin.readline().rstrip())
sortedN = sorted(N)[::-1]
for num in sortedN:
    print(num, end="")

# 다른 사람 코드
'''
print("".join(sortedN))
'''