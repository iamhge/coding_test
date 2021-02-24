# A+B - 3
T = int(input())
A = []

for i in range(T):
    A += map(int, input().split())

for i in range(T):
    print(A[i*2] + A[i*2 + 1])