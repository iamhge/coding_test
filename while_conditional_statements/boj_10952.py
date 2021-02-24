# A+B - 5
A = []
i = 0
while 1:
    A.append(tuple(map(int, input().split())))
    if (A[i][0] == 0 and A[i][1] == 0):
        break
    print(A[i][0]+A[i][1])
    i+=1