import sys
A = []
N = [0] * 10

for _ in range(3):
    A.append( int(sys.stdin.readline().rstrip()) )

mux = str(A[0] * A[1] * A[2])

for m in mux:
    for asc in range(48, 58):
        if (m == chr(asc)):
            N[asc - 48] += 1

for n in N:
    print(n)

# for i in range(10):
#     print(mux.count(str(i)))