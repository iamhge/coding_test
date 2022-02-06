# 주차 요금 계산
import math

def h2m(time):
    hh, mm = time.split(':')
    return int(hh)*60 + int(mm)

def solution(fees, records):
    answer = []
    IN = {}
    OUT = {}
    
    for record in records:
        record = record.split()
        if record[2] == 'IN':
            if record[1] not in IN:
                IN[record[1]] = []
                OUT[record[1]] = []
            IN[record[1]].append(h2m(record[0]))
            OUT[record[1]].append(1439)
        else:
            OUT[record[1]][-1] = (h2m(record[0]))
    
    for car in sorted(IN.keys()):
        usageTime = 0
        for i in range(len(IN[car])):
            usageTime += (OUT[car][i] - IN[car][i])
        if usageTime > fees[0]:
            answer.append(fees[1] + math.ceil((usageTime-fees[0])/fees[2]) * fees[3] )
        else:
            answer.append(fees[1])
    
    return answer