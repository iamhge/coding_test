# 달팽이는 올라가고 싶다
import sys

A, B, V = map(int, sys.stdin.readline().split())

# 마지막에는 결국 A 만큼 올라가게 되어있다.
# 따라서 V-A의 높이 만큼 A-B/day의 속도로 얼마나 걸리는 지 구한 후 +1
# 1 *((V - A) % (A - B) != 0) : 소수점이 있을 경우 올림 처리
day = (V - A) // (A - B) + 1 + 1 *((V - A) % (A - B) != 0)

print(day)