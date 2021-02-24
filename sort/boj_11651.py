# 좌표 정렬하기 2
# 방법 1
import sys

N = int(sys.stdin.readline().rstrip())
coordinate = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((y, x))

for y, x in sorted(coordinate):
    print(x, y)

# 방법 2
'''
import sys

N = int(sys.stdin.readline().rstrip())
coordinate = []
for _ in range(N):
    coordinate.append(tuple(map(int, sys.stdin.readline().split())))

for x, y in sorted(coordinate, key=lambda t : t[1]):
    print(x, y)
'''

# 다른 사람 코드
# itemgetter(1, 0) : 1번째로 정렬후 0번째로 정렬
# itemgetter 참고 : https://python.flowdas.com/howto/sorting.html
'''
from sys import stdin, stdout
from operator import itemgetter
read = stdin.readline

N = int(read())
pts = [tuple((map(int, read().split()))) for _ in range(N)]
pts = sorted(pts, key=itemgetter(1, 0)) 
stdout.write('\n'.join(f'{x} {y}' for x, y in pts))
'''