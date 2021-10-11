# 성적이 낮은 순서로 학생 출력하기
import sys

input = sys.stdin.readline

N = int(input().rstrip())
l = []
for i in range(N):
    l.append(tuple(input().split()))

for a, b in sorted(l, key=lambda x : x[1]):
    print(a, end=' ')