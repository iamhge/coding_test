# 01타일
'''
참고 : https://sungmin-joo.tistory.com/21
n = 1일 때 : 1
n = 2일 때 : 2
n = 3일 때 : 3
n = 4일 때 : 5
n = 5일 때 : 8
n = 6일 때 : 13
=> 피보나치 수열을 이룲
'''
import sys

N = int(sys.stdin.readline().rstrip())

fib = [1, 1]

for i in range(2, N + 1):
    fib.append((fib[i-2] + fib[i-1])%15746)

print(fib[N])