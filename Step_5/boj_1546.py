import sys

N = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().split()))

mscore = max(score)

for i in range(N):
    score[i] = score[i] / mscore * 100

print(sum(score)/len(score))