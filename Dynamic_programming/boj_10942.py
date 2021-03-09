# 팰린드롬?
'''
<개념>
  * 팰린드롬 : 회문. 
               거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자 문자열.
<아이디어>
  * 처음에 dp말고 다른 방법으로 풀고자했으나, 너무 같은 구간을 반복하고 비효율적이었다.
    그러한 비효율적인 방법 외에 도저히 모르겠어서 구글링
  * dp[start][end] : start에서부터 end까지의 팰린드롬 여부
  * dp[start+1][end-1] : 한 겹 안의 팰린드롬 여부
  * 길이가 1인, 2인, 3 이상인 경우로 각각 나누어서 생각해야 함.
  * 길이가 1인 경우 : 1
    길이가 2인 경우 : 서로 같으면 1
    길이가 3 이상인 경우 : dp[start+1][end-1]이 1이면 1 (한 겹 안이 팰린드롬인 경우)
<참고>
  [백준] 10942번(python 파이썬)
   : https://pacific-ocean.tistory.com/434
  백준알고리즘-10942번 팰린드롬?-파이썬(Python)
   : https://it-garden.tistory.com/352
'''
import sys

def solution(numList, N):
    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(N):
        for start in range(1, N+1):
            end = start + i

            if end > N:
                break
            if end == start:
                dp[start][end] = 1
                continue
            if numList[start] == numList[end]:
                # start + 1 == end : 한 개 차이 (ex. 11, 22, 33 ...)
                if start + 1 == end or dp[start+1][end-1] == 1: 
                    dp[start][end] = 1

    # for i in range(N):
    #     print(dp[i])
    return dp


def main():
    N = int(sys.stdin.readline().rstrip())
    numList = [0]
    numList.extend(list(map(int, sys.stdin.readline().split())))
    M  = int(sys.stdin.readline().rstrip())

    dp = solution(numList, N)                   

    for _ in range(M):
        S, E = map(int, sys.stdin.readline().split())
        print(dp[S][E])

if __name__=="__main__":
    main()
