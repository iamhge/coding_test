# 하노이의 탑
'''
ex)
n = 1
1 3

n = 2
1 2 -> n = 1, frm = 1, to = 2

1 3

2 3 -> n = 1, frm = 2, to = 3

n = 3
1 3
1 2
3 2 -> n = 2, frm = 1, to = 2

1 3

2 1
2 3
1 3 -> n = 2, frm = 2, to = 3
'''
def hanoi(n, frm, mid, to): # 개수, 출발지(from), 중간(mid), 도착지(to)
    result = []
    if n <= 1:
        return [[frm, to]]
    return hanoi(n-1, frm, to, mid) + [[frm, to]] + hanoi(n-1, mid, frm, to)

def solution(n):
    return hanoi(n, 1, 2, 3)