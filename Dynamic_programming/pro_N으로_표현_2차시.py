# N으로 표현 2차시
'''
- 또 못 풀어서 답 보고 풂
<풀이 방법>
  - N이 n개 사용됐을 경우를 모두 구한다. (n < 9)
    N이 n개 사용된 숫자
    = N이 1개 사용된 숫자 + N이 n-1개 사용된 숫자
    = N이 2개 사용된 숫자 + N이 n-2개 사용된 숫자
    = N이 3개 사용된 숫자 + N이 n-3개 사용된 숫자
    ...
    = N이 8개 사용된 숫자 + N이 n-8개 사용된 숫자
'''
def solution(N, number):
    answer = -1
    dp = [[]]
    
    for i in range(1, 9):
        cases = set()
        cases.add(int(str(N)*i))
        
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    cases.add(op1 + op2)
                    cases.add(op1 * op2)
                    cases.add(op1 - op2)
                    if op2 != 0:
                        if op1 % op2 == 0:
                            cases.add(op1 // op2)
        if number in cases:
            answer = i
            break
        dp.append(cases)
            
    return answer