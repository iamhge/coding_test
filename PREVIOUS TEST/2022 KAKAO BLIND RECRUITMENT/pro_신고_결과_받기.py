# 신고 결과 받기
def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}
    reported = {id: set() for id in id_list}
    for r in report:
        tmp = list(r.split())
        reported[tmp[1]].add(tmp[0])
    
    for key, val in reported.items():
        if len(val) >= k:
            for v in val:
                answer[v] += 1
                
    return list(answer.values())