import sys

N = int(sys.stdin.readline().rstrip())
route = 0

while N > 1 :
    N -= 6 * route
    route += 1

# N이 1이었을 경우
if route == 0:
    route += 1

print(route)