# 개미 전사
'''
a_n = (n+1번째 식량 창고까지 있을 때 얻을 수 있는 식량의 최댓값)
a_n = max(a_n-1, a_n-2 + K[n])
 * i 번째 식량 창고에 대한 최적의 해를 구할 때 부터 
   왼쪽부터 (i-3) 번째 이하의 식량 창고에 대한 최적의 해에 대해서는 고려할 필요가 없다.
'''
import sys

input = sys.stdin.readline

N = int(input().rstrip())
K = list(map(int, input().split()))
d = [0] * N

d[0] = K[0]
d[1] = max(K[1], K[0])

for i in range(3, N):
    d[i] = max(d[i-1], d[i-2] + K[i])

print(d[N-1])