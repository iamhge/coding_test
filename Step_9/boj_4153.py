import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if (a == b == c == 0):
        break
    hypotenuse = max(a, b, c)
    # 피타고라스
    if a**2 + b**2 + c**2 == 2*hypotenuse**2:
        print("right")
    else:
        print("wrong")