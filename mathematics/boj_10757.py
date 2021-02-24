# 큰 수 A+B
import sys

A, B = sys.stdin.readline().split()
A = list(map(int, list(A)))[::-1]
B = list(map(int ,list(B)))[::-1]

if (len(A) >= len(B)):
    B.extend([0]*(len(A) - len(B)))
else:
    A.extend([0]*(len(B) - len(A)))

answer = [0]*len(A)

for i in range(len(A)):
    answer[i] += A[i] + B[i]
    if answer[i] >= 10:
        answer[i] %= 10
        try: answer[i+1] = 1
        except: answer.append(1)

for i in range(len(answer), 0, -1):
    print(answer[i-1], end="")

# 파이썬은 그냥 잘 출력한다.. 묘하게 배신감드네..
'''
A, B = map(int, input().split())
print(A+B)
'''