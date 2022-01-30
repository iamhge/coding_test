# 오픈채팅방
ment = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

def solution(record):
    answer = []
    recordL = [r.split() for r in record]
    nickname = {}
    
    for r in recordL:
        if r[0] == "Leave": continue
        nickname[r[1]] = r[2]
    
    for r in recordL:
        if r[0] == "Change": continue
        answer.append(nickname[r[1]] + ment[r[0]])
    
    return answer