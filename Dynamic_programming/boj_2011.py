# 암호코드
'''
<아이디어>
  * dp[i][0]은 앞에서부터 i번째 자리까지만 봤을 때,
    암호화했을 때 나눠지는 결과의 맨 뒤 암호가 한 자리수 인 경우
    dp[i][1]은 앞에서부터 i번째 자리까지만 봤을 때,
    암호화했을 때 나눠지는 결과의 맨 뒤 암호가 두 자리수 인 경우
    ex) 2511
      dp[3][0] = 2 (2/5/1/1, 25/1/1)
      dp[3][1] = 2 (2/5/11, 25/11)
  * 앞에서부터 i번째 자리까지에서,
    맨 뒤의 두자리가 26초과면 -> dp[i][0] = dp[i-1][0]+dp[i-1][1] (i번째 수를 한자리 암호로만 추가)
                                dp[i][1] = 0
    맨 뒤의 두자리가 26이하면 -> dp[i][0] = dp[i-1][0]+dp[i-1][1] (i번째 수를 한자리 암호로 추가)
                                dp[i][1] = dp[i-1][0] (i번째 수를 두자리 암호로 추가)
<틀린 이유>
  1. 잘못된 암호 처리시, 0이 연속해서 두번 나오는 경우를 처리해주지 않음.
     이전 코드 : if N[i] == 0 and N[i-1] > 2:
     ex) 8100에서 틀린 답 1 나옴.
  2. if N[i] == 0 and N[i-1] != 1 and N[i-1] != 2: 에서
     이전 코드 : if N[i] == 0 and N[i-1] != (1 or 2): 로 했음.
     ex) 20에서 틀린 답 0 나옴.
'''
import sys

def numOfPW(N: list) -> int:
    # 가장 높은 자리수가 0이면 잘못된 암호
    if N[0] == 0:
        return 0

    dp = [[0]*2 for _ in range(len(N))]
    dp[0][0] = 1

    for i in range(1, len(N)):
        # 잘못된 암호
        if N[i] == 0 and N[i-1] != 1 and N[i-1] != 2:
            return 0

        if N[i-1]*10 + N[i] == 10 or N[i-1]*10 + N[i] == 20:
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0]+dp[i-1][1]
            if N[i-1]*10 + N[i] <= 26:
                dp[i][1] = dp[i-1][0]
            else:
                dp[i][1] = 0

    return sum(dp[len(N)-1]) % 1000000

def main():
    N = list(map(int, list(sys.stdin.readline().rstrip())))
    print(numOfPW(N))

if __name__=="__main__":
    main()

# 다른 사람 코드
# 피보나치 수열 형태 이용
# 한 자리 수 : dp[i-1]
# 두 자리 수 : dp[i-2]
'''
a = list(map(int, list(input())))
l = len(a)

# dp[i] : i번째 수 단계에서 암호 코드의 개수
dp = [0] * (l+1)

if a[0] == 0: # 암호 만들 수 없는 경우
    print(0)
else :
    a = [0] + a # 인덱싱을 위해 추가한 0
    dp[0] = 1
    dp[1] = 1 # 첫번째 수로 이뤄진 암호코드는 1개이다.

    for i in range(2, l+1):
        cur = a[i] # 한 자리
        cur2 = a[i-1] * 10 + a[i] # 두 자리
        if cur >= 1 and cur <= 9:
            dp[i] += dp[i-1]
        if cur2 >= 10 and cur2 <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000

    print(dp)
    print(dp[l])
    '''