import sys

box = []

for i in range(3):
    box.append( list(map(int, sys.stdin.readline().split())) )

l = min(box[i][0] for i in range(3))
r = max(box[i][0] for i in range(3))
d = min(box[i][1] for i in range(3))
u = max(box[i][1] for i in range(3))

if [l, d] not in box:
    print(l, d)
elif [l, u] not in box:
    print(l, u)
elif [r, d] not in box:
    print(r, d)
else:
    print(r, u)

# 다른 사람 코드 (조건문으로 어디 점인지 파악해서 찍음)
'''
def fsn(x, y, z):
    if x == y: return z
    elif x == z: return y
    else: return x

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

print(fsn(a, c, e), fsn(b, d, f))
'''