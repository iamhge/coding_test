# 손익분기점
import sys

A, B, C = map(int, sys.stdin.readline().split())

# 생산 대수를 늘려도 이익이 나지 않을 경우
# C * (BEP + 1) - (A + B * (BEP + 1)) <= C * BEP - (A + B * (BEP))
# 위 식에서 BEP가 0일 경우로 정리하면 아래와 같음 
# 사실 가변비용 B가 가격 C보다 작으면 당연히 적자.
if C - B <= 0:
    BEP = -1
else: # C * BEP - (A + B * BEP) > 0 식을 정리하면 아래와 같음
    BEP = A // (C - B) + 1 

# Break-Even Point
print(BEP)