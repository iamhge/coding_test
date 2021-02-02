import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dist = ((x1 - x2)**2 + (y1- y2)**2)**0.5

    if dist == 0 and r1 == r2: # 두 원이 같음
        print("-1")
    elif dist < r1 + r2 and dist > abs(r1 - r2): # 두 원이 두 점에서 만남
        print('2') 
    elif dist == r1 + r2 or dist == abs(r1 - r2): # 두 원이 한 점에서 만남 (1. 밖으로, 2. 내접)
        print('1')
    else: # 두 원이 멀리 떨어져있음
        print('0')
