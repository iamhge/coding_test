# 평균은 넘겠지
import sys

C = int(sys.stdin.readline().rstrip())

for _ in range(C):
    N, *scores = map(int, sys.stdin.readline().split())
    overMean = 0
    mean = sum(scores)/len(scores)
    for score in scores:
        if score > mean:
            overMean += 1
    print("%.3f%%" %( overMean/N*100 ))