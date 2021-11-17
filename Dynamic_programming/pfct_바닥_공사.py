# 바닥 공사
'''
a_n = (2xn 크기의 바닥을 채우는 방법의 수)

a_1 = 1
a_2 = 3
a_3 = 5
a_4 = a_2 * 2 + a_3 
...
a_n = a_n-2 * 2 + a_n-1

해설)
a_n-2의 뒤에 1 X 2를 두 개 놓는 경우 
    + a_n-2의 뒤에 2 X 2를 놓는 경우
    + a_n-1의 뒤에 2 X 1을 한 개 놓는 경우
'''
import sys

input = sys.stdin.readline

N = int(input().rstrip())
d = [0] * N

d[0] = 1
d[1] = 3

for i in range(2, N):
    d[i] = d[i-2] * 2 + d[i-1]

print(d[N-1] % 796796)