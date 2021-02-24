# 나머지
import sys

M = []
r = 0

for i in range(10):
    N = int(sys.stdin.readline().rstrip())
    N %= 42
    if (M.count(N) == 0):
        r += 1
    M.append(N)

print(r)

# 다른 사람 코드 (집합 이용)
'''
ans = set()
for i in range(0,10):
    n = input()
    # 집합형 자료형
    ans.add(int(n) % 42)
print(len(ans))
'''