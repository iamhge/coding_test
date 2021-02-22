# 회의실 배정
'''
<아이디어>
  첨에 Shortest job first 생각했으나, 시간 초과. 최적해 찾는지도 모르겠음.
  끝나는 시간을 기준으로 정렬해야한다.
<Q&A>
  Q. 시작 시간 기준, 끝나는 시간 기준 두번 정렬하는 이유 
  A. 둘 중 하나로만 정렬하면, 시작동시에 끝나는 경우를 커버 못함.
     ex) 10 10 과 1 10
     끝나는 시간 기준으로만 정렬시, 
     10 10 다음으로 1 10이 선택되지 않는다. (10(scheduleEnd) < 1(s)이므로)
     ex) 1 1 과 1 10
     시작 시간 기준으로만 정렬시,
     1 10 다음으로 1 1이 선택되지 않는다. (10(scheduleEnd) < 1(s)이므로)
<참고>
  [백준 1931번 회의실배정] 문제 해설 - 파이썬
   : https://covenant.tistory.com/126
  알고리즘 수업 자료 lec4
'''
import sys

N = int(sys.stdin.readline().rstrip())
time = []
scheduleEnd = 0
conference = 0

for _ in range(N):
    time.append(tuple(map(int, sys.stdin.readline().split())))

# 끝나는 시간으로 정렬하되, 그 안에서 시작하는 시간 순으로 정렬
time.sort(key= lambda x : (x[1], x[0]))

for s, e in time:
    if s >= scheduleEnd:
        scheduleEnd = e
        conference += 1

print(conference)

# 짧은 작업 우선
# 시간초과 남.
'''
import sys

def checkSchedule(schedule: list, start: int, end: int)->bool:
    for i in range(start, end):
        if i in schedule:
            return False
    return True

def addToSchedule(schedule: list, start: int, end: int)->list:
    for i in range(start, end):
        schedule.append(i)
    return schedule

N = int(sys.stdin.readline().rstrip())
time = []
schedule = []
conference = 0

for _ in range(N):
    time.append(tuple(map(int, sys.stdin.readline().split())))

time.sort(key= lambda x : x[1]-x[0])

for i in range(N):
    if checkSchedule(schedule, time[i][0], time[i][1]):
        schedule = addToSchedule(schedule, time[i][0], time[i][1])
        conference += 1

print(conference)
'''