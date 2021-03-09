# 카드 구매하기
'''
<아이디어>
  * dp[i] : i개의 카드를 사기 위한 금액의 최댓값 
'''
import sys
import copy

def solution(N: int, P: list):
    dp = copy.deepcopy(P)

    for i in range(2, N+1):
        for j in range(1, i//2+1):
            dp[i] = max(dp[i], dp[i-j] + dp[j])
    
    return dp[N]

def main():
    N = int(sys.stdin.readline().rstrip())
    P = [0]
    P.extend(list(map(int, sys.stdin.readline().split())))

    print(solution(N, P))

if __name__=="__main__":
    main()