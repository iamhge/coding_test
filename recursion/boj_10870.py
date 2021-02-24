# 피보나치 수 5
# 내 코드
import sys

# 재귀
def fibonacci(N: int):
    if N < 2:
        return N
    return fibonacci(N-1) + fibonacci(N-2)

# 반복문 (시간 복잡도 낮음)
def fibonacci_2(N: int):
    if N < 2:
        return N
    current = 1
    last = 0
    for _ in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

n = int(sys.stdin.readline().rstrip())
print(fibonacci(n))

# 다른 사람 코드 (반복문을 배열로 해결)
'''
n = int(input())
s = [0, 1]
for i in range(2, n + 1):
    s.append(s[i - 1] + s[i - 2])
print(s[n])
'''