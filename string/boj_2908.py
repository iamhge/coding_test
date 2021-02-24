# 상수
import sys
'''
A, B = map(str, sys.stdin.readline().split())
A = list(A)
B = list(B)

temp = A[0]
A[0] = A[2]
A[2] = temp

temp = B[0]
B[0] = B[2]
B[2] = temp

A = ''.join(A)
B = ''.join(B)

print(max(int(A), int(B)))
'''

# 다른 사람 코드
A, B = map(str, sys.stdin.readline().split())
# 처음부터 끝까지 -1칸 간격으로 == 역순으로
A = A[::-1]
B = B[::-1]

print(max(A, B))