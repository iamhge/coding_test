import sys
N, X = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
for elem in li:
    if elem < X:
        print(elem, end=' ')