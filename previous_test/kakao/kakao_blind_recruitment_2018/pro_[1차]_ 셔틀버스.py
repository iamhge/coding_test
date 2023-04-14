# 셔틀버스
from collections import deque

def time2minute(time):
    hh, mm = map(int, time.split(':'))
    return hh*60 + mm

def minute2time(minute):
    hh = "00" + str(minute//60)
    mm = "00" + str(minute%60)
    return hh[-2:] + ":" + mm[-2:]

def solution(n, t, m, timetable):
    # 시간 타입 변경
    myTimetable = []
    for time in timetable:
        myTimetable.append(time2minute(time))
    myTimetable.sort()
    
    queue = deque(myTimetable)
    departTime = time2minute("09:00")-t
    
    # departInfo[departTime] = [마지막 탑승자의 탑승 시각, 남은 탑승 가능 인원 수]
    departInfo = {}
    
    for i in range(n):
        departTime += t # 셔틀 출발 시간
        remain = m # 남은 좌석 수
        
        while queue:
            if queue[0] > departTime:
                break
            if remain <= 0:
                break
            
            remain -= 1
            departInfo[departTime] = [queue.popleft(), remain]

    # 마지막 출발 시간에 아무도 탑승하지 않으면 or 자리가 남아있으면
    # 마지막 출발 시간에 정류장에 도착한다.
    if departTime not in departInfo or departInfo[departTime][1] > 0:
        return minute2time(departTime)
    
    # 마지막 출발 시간에 자리가 없으면 마지막 출발 시간의 마지막 탑승자보다 1분 빨리 탑승한다.
    return minute2time( departInfo[departTime][0]-1 )