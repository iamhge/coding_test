# 기능개발
def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    
    prev = (100 - progresses[0] + (speeds[0]-1)) // speeds[0]
    count = 1
    for i in range(1, N):
        time = (100 - progresses[i] + (speeds[i]-1)) // speeds[i]
        if prev >= time:
            count += 1
        else:
            prev = time
            answer.append(count)
            count = 1
    
    answer.append(count)
    
    return answer

# 다른 사람 풀이
'''
stack에 맞는 풀이
'''
'''
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
'''