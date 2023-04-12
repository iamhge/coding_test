# 추석 트래픽
'''
<오답 노트>
- 처리시간은 시작시간과 끝시간을 포함!!!!! 을 제대로 생각 못했다.
- start 전 1초 동안 처리량, start 후 1초 동안 처리량, end 전 1초 동안 처리량, end 후 1초 동안 처리량 중 
  마지막 end 후 1초 동안 처리량만 구해도 된다.
  why? end(S) 기준으로 정렬되어 있어서 end가 무조건 다음 태스크보다 작다.
<참고>
구분자 여러개로 string to list
: https://velog.io/@highgrace/구분자-여러개로-string-to-list
'''

import re

# S를 ms 단위로 변환한다.
def S2ms(S):
    hh, mm, ss, sss = map(int, re.split('[:|.]', S))
    return hh*60*60*1000 + mm*60*1000 + ss*1000 + sss

# T를 ms 단위로 변환한다.
def T2ms(T):
    return int(float(T[:-1])*1000)

def solution(lines):
    answer = 0
    myST = []
    
    _, S, T = lines[0].split(" ")
    
    for line in lines:
        _, S, T = line.split(" ")
        myST.append([S2ms(S), T2ms(T)])
    
    for i in range(len(myST)):
        start = myST[i][0] - myST[i][1] + 1
        end = myST[i][0]
        
        # end 후 1초 동안 처리량
        throughput = 0
        
        for j in range(len(myST)):
            logStart = myST[j][0] - myST[j][1] + 1
            logEnd = myST[j][0]
            if not (logEnd < end or end + 999 < logStart):
                throughput += 1
        answer = max(answer, throughput)
    
    return answer