# 후보키
from itertools import combinations

def isCandidateKey(key, relation, combis, notValid, answer):
    now = []
    for r in relation:
        attributes = tuple(r[k] for k in key)
        if attributes not in now:
            now.append(attributes)
        else:
            break
    else: # key가 후보키인 경우
        answer += 1
        for combi in combis:
            for k in key:
                if k not in combi: break
            else:
                # 최소성을 만족하지 않는 것들 추가
                notValid.append(combi)
        
    return notValid, answer 

def solution(relation):
    answer = 0
    combis = []
    notValid = []
    
    for i in range(1, len(relation)+1):
        combis.extend(list(combinations([j for j in range(len(relation[0]))], i)))
        
    for combi in combis:
        if combi not in notValid:
            notValid, answer = isCandidateKey(combi, relation, combis, notValid, answer)
    
    return answer