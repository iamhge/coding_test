# 광고 삽입
'''
- 다른 사람 코드 참고
<풀이 방법>
  - 누적 합
  - 두 번 누적합을 하는데, 이유는 다음과 같다.
    1) 첫 누적합은 각 시간대 별 시청자 수를 나타내기 위함이다.
    2) 두번째 누적합은 누적 시청 기록을 구하기 위함이다.
<소감>
  - 될 것 같았지만 아이디어를 떠올리지 못해 시간이 오래 걸리는 등 문제가 많았다.
  - 참고 링크를 통해 아이디어를 얻고도, 경곗값 분석이 힘들어 문제 풀이에 시간이 걸렸다.
<참고>
  [프로그래머스] 광고 삽입 / Python
  : https://dev-note-97.tistory.com/156#--%--logs%--%EB%--%B-%EC%-D%--%--%EB%AA%A-%EB%--%A-%--%EC%-B%-C%EA%B-%--%--%EC%B-%--%EB%A-%-C%--%ED%--%--%EC%--%B-%--%EB%B-%-F%--start%-C%--end%--%EA%B-%AC%EB%B-%--
'''
def timeToSec(time):
    sec = 0
    for idx, num in enumerate(time.split(":")):
        sec += int(num) * 60 ** (2-idx)
    return sec

def secToTime(sec):
    time = []
    
    time.append( ("0" + str(sec // 3600))[-2:] )
    minSec = sec % 3600
    time.append( ("0" + str(minSec // 60))[-2:])
    time.append( ("0" + str(minSec % 60))[-2:] )
    
    return ':'.join(time)

def solution(play_time, adv_time, logs):
    answer = ''
    myLogs = []
    myPT = timeToSec(play_time)
    myAT = timeToSec(adv_time)
    maxAccumulateTime = -1
    clock = [0] * (myPT + 1)
    
    for log in logs:
        myLog = [timeToSec(time) for time in list(log.split('-'))]
        clock[myLog[0]] += 1
        clock[myLog[1]] -= 1
    
    for i in range(myPT):
        clock[i+1] += clock[i]
        
    for i in range(myPT):
        clock[i+1] += clock[i]
    
    for i in range(myPT - myAT + 1):
        if i == 0:
            accumulateTime = clock[i + myAT - 1]
        else:
            accumulateTime = clock[i + myAT - 1] - clock[i-1]
        
        if maxAccumulateTime < accumulateTime:
            maxAccumulateTime = accumulateTime
            answer = secToTime(i)
            
    return answer
'''
<풀이 방법>
  1) clock = 광고 시작시간.
  2) clock을 처음부터 끝까지 돌리고, 각각에서 누적 시간을 구한다.
  3) 누적 시간 최대일 때의 clock을 구한다.
  -> 시간 초과
'''
'''
def timeToSec(time):
    sec = 0
    for idx, num in enumerate(time.split(":")):
        sec += int(num) * 60 ** (2-idx)
    return sec

def secToTime(sec):
    time = []
    
    time.append( ("0" + str(sec // 3600))[-2:] )
    minSec = sec % 3600
    time.append( ("0" + str(minSec // 60))[-2:])
    time.append( ("0" + str(minSec % 60))[-2:] )
    
    return ':'.join(time)

def solution(play_time, adv_time, logs):
    answer = ''
    myLogs = []
    myPT = timeToSec(play_time)
    myAT = timeToSec(adv_time)
    maxAccumulateTime = 0
    
    for log in logs:
        myLogs.append([timeToSec(time) for time in list(log.split('-'))])
    myLogs.sort()
    
    for clock in range(myPT - myAT + 1):
        end = clock + myAT
        accumulateTime = 0
        
        for myLog in myLogs:
            if myLog[1] <= clock: continue
            if myLog[0] >= end: continue
            accumulateTime += min(end, myLog[1]) - max(clock, myLog[0])
        
        if maxAccumulateTime < accumulateTime:
            answer = secToTime(clock)
            maxAccumulateTime = accumulateTime
            
    return answer
'''
# 틀린 코드
'''
<틀린 이유>
  - 시작시간을 무조건 logs의 시작시간에 맞췄는데, 이렇게 하면 최적을 찾을 수 없다.
  - log의 끝 시간에 맞춰야 최적이 될 수도 있고, 중간에 있을 수도 있다.
'''
'''
def timeToSec(time):
    sec = 0
    for idx, num in enumerate(time.split(":")):
        sec += int(num) * 60 ** (2-idx)
    return sec

def secToTime(sec):
    time = []
    
    time.append( ("0" + str(sec // 3600))[-2:] )
    minSec = sec % 3600
    time.append( ("0" + str(minSec // 60))[-2:])
    time.append( ("0" + str(minSec % 60))[-2:] )
    
    return ':'.join(time)

def solution(play_time, adv_time, logs):
    answer = ''
    myLogs = []
    myPT = timeToSec(play_time)
    myAT = timeToSec(adv_time)
    maxAccumulateTime = 0
    
    for log in logs:
        myLogs.append([timeToSec(time) for time in list(log.split('-'))])
    myLogs.sort()
    
    for idx, myLog in enumerate(myLogs):
        if myLog[0] + myAT > myPT:
            start = myPT - myAT
            end = myPT
        else:
            start = myLog[0]
            end = myLog[0] + myAT
        
        accumulateTime = 0
        for i in range(idx-1, -1, -1):
            if myLogs[i][1] < start: break
            accumulateTime += min(end, myLogs[i][1]) - start
        for i in range(idx, len(myLogs)):
            if end < myLogs[i][0]: break
            accumulateTime += end - max(start, myLogs[i][0])
            
        if maxAccumulateTime < accumulateTime:
            answer = secToTime(start)
            maxAccumulateTime = accumulateTime
            
    return answer
'''