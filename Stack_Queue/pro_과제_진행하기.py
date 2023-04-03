# 과제 진행하기
'''
<소감>
  - 
  - 다른 사람 풀이를 확인하면, hh:mm을 그냥 분으로 환산하여 쉽게 계산함.
    addTime, getTimegap 함수를 만들 것 없이 그렇게 했으면 더 간결한 코드가 만들어졌을 것.
'''
from collections import deque

def addTime(now, playtime):
    answer = ""
    hour, minute = map(int, now.split(":"))
    minute += int(playtime)
    
    if minute // 60 >= 1:
        hour += minute // 60
        minute %= 60
    if hour < 10:
        answer += "0" + str(hour)
    else:
        answer += str(hour)
    answer += ":"
    
    if minute< 10:
        answer += "0" + str(minute)
    else:
        answer += str(minute)
        
    return answer 

# a < b
def getTimegap(a, b):
    gap = 0
    aHour, aMin = map(int, a.split(":"))
    bHour, bMin = map(int, b.split(":"))
    
    gap += (bHour - aHour) * 60
    gap += bMin - aMin
    return gap

def solution(plans):
    answer = []
    stack = deque([])
    
    # start 순으로 정렬
    plans.sort(key = lambda x: x[1])
    
    # 첫 번째 과제
    end = addTime(plans[0][1], plans[0][2])
    stack.append([plans[0][0], int(plans[0][2])])

    # for plan in plans:
    for i in range(1, len(plans)):
        before, _ = stack.pop()
        
        # 새 과제
        name, start, playtime = plans[i]
    
        # 하던 과제를 관둬야 할 때
        if end > start:
            stack.append([before, getTimegap(start, end)])
        # 멈춰둔 과제를 진행할 때
        else:
            # 하던 과제 끝
            answer.append(before)
            
            # 멈춰둔 과제 진행
            while stack:
                stop, remain = stack.pop()
                end = addTime(end, remain)
                # 멈춰둔 과제 완료
                if end <= start:
                    answer.append(stop)
                # 멈춰둔 과제 완료 불가
                else:
                    stack.append([stop, getTimegap(start, end)])
                    break
        
        # 새 과제 진행
        stack.append([name, int(playtime)])
        end = addTime(start, playtime)
        
    while stack:
        answer.append(stack.pop()[0])
        
    return answer

# 다른 사람 풀이
'''
def solution(plans):
    answer = []
    arr = []
    for plan in plans:
        name = plan[0]
        h, m = map(int, plan[1].split(':'))
        t = int(plan[2])
        arr.append((name, h*60 + m, t))

    arr.sort(key= lambda x : x[1])
    st = []
    for i in range(len(arr)-1):
        n, s, t = arr[i]
        if s + t <= arr[i+1][1]:
            answer.append(n)
            tot = arr[i+1][1] - s - t
            while st:
                name, time = st.pop()
                if tot >= time:
                    tot -= time
                    answer.append(name)
                else:
                    st.append((name, time - tot))
                    break

        else:
            st.append((n, t - (arr[i+1][1] - s)))
    answer.append(arr[-1][0])

    while st:
        answer.append(st.pop()[0])
    return answer
'''