# 블랙잭
import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

opt = M

for c1 in range(N):
    for c2 in range(c1+1, N):
        for c3 in range(c2+1, N):
            diff = M - (card[c1] + card[c2] + card[c3])
            if diff >= 0 and diff < opt:
                opt = diff

print(M - opt)