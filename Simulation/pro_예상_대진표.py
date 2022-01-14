# 예상 대진표
def numbering(a, b):
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b += 1
    return a, b

def solution(n,a,b):
    answer = 1
    a, b = numbering(a, b)
    while abs(a-b) > 1:
        a //= 2
        b //= 2
        answer += 1
        a, b = numbering(a, b)
    return answer