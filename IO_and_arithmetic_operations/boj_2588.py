# 곱셈
'''
A = int(input())
B = list(map(int, list(input())))

print(A * B[2])
print(A * B[1])
print(A * B[0])
print(A * B[2] + (A * B[1])*10 + (A * B[0])*100)
'''

A = int(input())
B = int(input())

print(A*(B%10))
print(A*(B%100//10))
print(A*(B//100))
print(A*B)