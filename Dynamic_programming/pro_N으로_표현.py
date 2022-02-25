# N으로 표현
'''
<풀이 방법>
  - N이 n개 사용됐을 경우를 모두 구한다. (n < 9)
  - N이 n개 사용된 숫자
    = N이 1개 사용된 숫자 + N이 n-1개 사용된 숫자
    = N이 2개 사용된 숫자 + N이 n-2개 사용된 숫자
    ...
    = N이 8개 사용된 숫자 + N이 n-8개 사용된 숫자
    ※ 이때 +는 덧셈이 아닌 사칙 연산을 의미한다. 사칙 연산에서 -, / 는 앞 뒤가 바뀌면 해가 달라지므로, 8까지 모두 검사한다.
<참고>
  프로그래머스 문제 풀이 N으로 표현
  : https://gurumee92.tistory.com/164
  N으로 표현 - PYTHON
  : https://velog.io/@j_user0719/N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-PYTHON
  
ps. 제한 사항에서 최솟값이 8보다 크면 -1 리턴하는거 못보고 recursion 에러로 헤맴 ㅡㅡ
'''

def solution(N, number):
    answer = -1
    dp = [[]] # dp[n] : n개의 N으로 만든 수의 배열
    
    for i in range(1, 9): # N의 개수
        cases = set()
        cases.add(int(str(N) * i)) # N, NN, NNN, ...
        
        for j in range(i):
            for op1 in dp[j]: 
                for op2 in dp[i-j]:
                    cases.add(op1 - op2)
                    cases.add(op1 + op2)
                    cases.add(op1 * op2)
                    if op2 != 0:
                        cases.add(op1 // op2)
        
        if number in cases:
            answer = i
            break
        
        dp.append(cases)
    
    return answer