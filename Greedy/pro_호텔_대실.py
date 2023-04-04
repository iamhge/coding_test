# 호텔 대실
'''
<요약>
* 최소한의 객실
* 10분 후 다음 손님
<풀이 방법>
* 그리디 알고리즘
'''

def time2min(time):
    hour, minute = map(int, time.split(":"))
    return hour*60 + minute

def solution(book_time):
    answer = 0
    room = [] # room[i] = i번 room의 out 시간 + 10분
    book_time.sort(key = lambda x: x[0])
    
    for bt in book_time:
        start = time2min(bt[0])
        end = time2min(bt[1]) + 10 # 10분 후부터 가능하므로
        for i in range(len(room)):
            if room[i] <= start:
                room[i] = end
                break
        else:
            room.append(end)
    
    return len(room)


# 다른 사람 풀이
'''
* 누적합으로 풀이함.
* 이 방법이 이중 for문을 쓰지 않아 더 적합한 풀이로 보임!!!!!
'''
'''
def time2min(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    minute = [0 for _ in range(24*60 + 10)]

    for book in book_time:
        start = time2min(book[0])
        end = time2min(book[1])
        minute[start] += 1
        minute[end+10] += -1
    num = 0
    for i in range(len(minute)):
        num += minute[i]
        minute[i] = num

    answer = max(minute)

    return answer
'''