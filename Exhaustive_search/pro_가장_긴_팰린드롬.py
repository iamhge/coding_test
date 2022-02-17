# 가장 긴 팰린드롬
# 가장 긴 팰린드롬
'''
<문제 정보>
  - boj_10942.py(백준 10942 - 팰린드롬?)와 유사한 문제 -> 해당 문제 풀이방법 참고
<풀이 방법>
  - boj_10942.py(백준 10942 - 팰린드롬?) 참고
  * dp[start][end] : start에서부터 end까지의 팰린드롬 여부
  * dp[start+1][end-1] : 한 겹 안의 팰린드롬 여부
  * 길이가 1인, 2인, 3 이상인 경우로 각각 나누어서 생각해야 함.
  * 길이가 1인 경우 : 1
    길이가 2인 경우 : 서로 같으면 2
    길이가 3 이상인 경우 : dp[start+1][end-1]이 1이상이면 dp[start+1][end-1] + 2 (한 겹 안이 팰린드롬인 경우)
<효율성 테스트 결과>
  테스트 1 〉	통과 (1342.92ms, 58.1MB)
  테스트 2 〉	통과 (1579.08ms, 97MB)
  -> 첫 풀이 방법이 마음에 안들어서 바꾼 방법인데, 오히려 더 오래걸린다.. 풀이 방법 다시 공부한 셈 치자.
'''

def solution(s):
    answer = 1
    dp = [[0]*len(s) for _ in range(len(s))]
    
    for i in range(len(s)):
        for start in range(len(s)):
            end = start + i
            
            if end >= len(s):
                 break
            if end == start:
                dp[start][end] = 1
                continue
            if s[start] == s[end]:
                if start + 1 == end: # 1개 차이로 팰린드롬인 경우
                    dp[start][end] = 2
                if dp[start+1][end-1] >= 1: # 한 겹 안이 팰린드롬인 경우
                    dp[start][end] = dp[start+1][end-1] + 2
            answer = max(answer, dp[start][end])

    return answer

# 정답이지만 마음에 안드는 풀이 방법
'''
<풀이 방법>
  (dp라고 썼지만) 단순 브루트포스
  - dp[i] = i번째 문자를 기준으로 팰린드롬의 길이
  - 문자 하나하나를 기준으로 팰린드롬의 최대 길이를 구한다.
  - 팰린드롬의 길이가 짝수인 경우 s의 앞 뒤를 검사하는 방법으로 해결되지 않는다.
    -> 문자의 사이에서도 앞 뒤를 검사하도록 한다.
    -> s_ = s의 문자 사이사이에 띄어쓰기를 넣은 문자열
<효율성 테스트 결과>
  테스트 1 〉	통과 (5.93ms, 10.3MB)
  테스트 2 〉	통과 (887.85ms, 10.2MB)
'''
'''
def solution(s):
    dp = [1, 0] * len(s)
    s_ =''
    for c in s:
        s_+= c + ' '
    
    for i in range(1, len(s_)-1):
        for j in range(1, i+1):
            if i+j >= len(s_): break
            if s_[i-j] != s_[i+j]: break
            if s_[i-j] != ' ':
                dp[i] += 2

    return max(dp)
'''