import sys

S = sys.stdin.readline().rstrip()
time = 0
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

for c in S:
    for i in range(len(dial)):
        if dial[i].find(c) != -1:
            time += i+3
            break

print(time)