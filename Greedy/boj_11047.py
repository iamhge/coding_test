# 동전 0
'''
문제 조건 
: N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
  (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
=> greedy로 못 푸는 경우를 생각하지 않아도 됨.
greedy로 못 푸는 경우 ex)
K = 14 
동전 : 10 8 7 1 
greedy로 풀 때) 10 + 1*4 -> 5개
실제 최적) 7*2 -> 2개
'''
import sys

N, K = map(int, sys.stdin.readline().split())
A = []
num = 0

for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip()))
A.sort(reverse=True)

for i in A:
    if i <= K:
        num += K // i
        K = K % i
    if K == 0:
        break

print(num)