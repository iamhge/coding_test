# 양궁대회
# 2차시
from itertools import combinations_with_replacement

def calScore(apeach, lion):
    aScore = 0
    lScore = 0
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0: continue
        elif apeach[i] < lion[i]:
            lScore += 10-i
        else:
            aScore += 10-i
    return lScore - aScore

def solution(n, info):
    answer = [-1]
    maxScore = 0
    
    for combi in sorted(list(combinations_with_replacement([i for i in range(11)], n)), key = lambda x: x[::-1], reverse = True):
        lionInfo = [0] * 11
        for c in combi:
            lionInfo[c] += 1

        lscore = calScore(info, lionInfo)
        
        if lscore > maxScore:
            maxScore = lscore
            answer = lionInfo
    
    return answer