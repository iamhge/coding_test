# 스티커
'''
<아이디어>
  * 각 위치에 대한 dp값은 자기자신을 포함했을 때 가장 큰 score값을 나타냄.
  * n번째 라인의 경우, n-1번째 라인의 대각선에 위치한 dp값 + 자신의 score
                      혹은 n-2번째 라인에서 큰 dp값 + 자신의 score 
    가 dp값이 된다.
<해경이의 뇌피셜 Q&A>
  Q. n-2번째 라인까지만 검사하는 이유?
  A. n-3번째 이하 라인에서 큰 dp값 + 자신의 score는 최댓값이 될 수 없다. 
     중간에 무조건 스티커 하나이상 더 뗄 수 있기 때문.
'''
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    score = []
    dp = [[0]*n for _ in range(2)]
    for __ in range(2):
        score.append(list(map(int, sys.stdin.readline().split())))
    
    dp[0][0] = score[0][0]
    dp[1][0] = score[1][0]

    if n >= 2:
        dp[0][1] = score[1][0] + score[0][1]
        dp[1][1] = score[0][0] + score[1][1]

    for j in range(2, n):
        for i in range(2): # 열을 우선으로 루프를 순회한다.
            dp[i][j] = max(dp[1-i][j-1], max(dp[i][j-2], dp[1-i][j-2])) + score[i][j]
    
    print(max(map(max, dp)))

# 다른 사람 코드
# dp 리스트를 사용하지 않고, 변수 세개로 해결
# pick1_value : 위에서 선택한 경우
# pick2_value : 아래 줄에서 선택한 경우
# not_pick_value : 해당 줄(열)에서는 모두 선택하지 않은 경우
'''
def max_value (list1, list2):
    length = len(list1)
    if length != len(list2):
        print("두 리스트의 길이가 다릅니다.")
        return 0
    pick1_value = list1[0]
    pick2_value = list2[0]
    not_pick_value = 0
    #1번 리스트 선택했을때 최댓값, 2번 리스트 선택했을때 최댓값, 안선택했을때 최댓값
    for i in range(1,length):
        temp1 = pick1_value # 1번 리스트 선택 이전값 저장
        temp2 = not_pick_value # 안선택했을때 이전값 저장
        not_pick_value = max(pick1_value,pick2_value)
        pick1_value = max(temp2,pick2_value) + list1[i]
        pick2_value = max(temp2,temp1) + list2[i]
    value = max(pick1_value, pick2_value)
    return value

if __name__ == '__main__':
    count = int(input())
    result = []
    for i in range(count):
        list_length = int(input())
        temp_list1 = [int(i) for i in input().split()]
        temp_list2 = [int(i) for i in input().split()]
        temp = max_value (temp_list1, temp_list2)
        result.append(temp)
    for i in result:
        print(i)

'''