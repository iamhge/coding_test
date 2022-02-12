# 최고의 집합
def solution(n, s):
    base = s // n
    if base < 1:
        return [-1]
    answer = [base for _ in range(n-s%n)]
    for _ in range(s%n):
        answer.append(base + 1)
    return answer