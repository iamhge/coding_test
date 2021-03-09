# 앱
'''
<아이디어>
  * 냅색 top-down방식 이용.
  * dp[i] : 메모리를 i만큼 비워야할 때 드는 최소 비용
<틀린 이유>
  1. 시간 초과 -> pypy3으로 제출하니 맞음.
'''
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    mem = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    
    dp = [sum(c)]*(sum(mem)+1)
    dp[0] = 0
    
    memCount = 0
    for i in range(0, N):
        memCount += mem[i]
        for j in range(memCount, -1, -1):
            if j <= mem[i]:
                dp[j] = min(c[i], dp[j])
            else:
                dp[j] = min(dp[j - mem[i]] + c[i], dp[j])

    print(dp[M])

if __name__=="__main__":
    main()

# 다른 사람 코드
# cost를 기준으로 순회
# dp[i] : cost가 i인 경우, 최대로 비울 수 있는 메모리 크기
# cost의 범위가 0~100이고, mem의 범위가 1~10000000 이므로, 아래 방법이 더 빠르다.
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mem = [*map(int, input().split())]
cost = [*map(int, input().split())]

cost_max = sum(cost)
dp = [-1] * (cost_max+1)
dp[0] = 0
for i in range(n):
    for j in range(cost_max - cost[i], -1,-1):
        if dp[j] != -1:
            dp[j + cost[i]] = max(dp[j + cost[i]], dp[j] + mem[i])

for i in range(cost_max + 1):
    if dp[i] >= m:
        print(i)
        break
'''