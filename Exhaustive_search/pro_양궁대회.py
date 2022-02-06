# 양궁대회
from itertools import combinations_with_replacement

def scoreCal(a, l):
    aScore, lScore = 0, 0
    for i in range(11):
        if a[i] == 0 and l[i] == 0: continue
        if a[i] >= l[i]: aScore += 10-i
        else: lScore += 10-i
    return lScore - aScore

def solution(n, info):
    answer = [-1]
    maxScore = -1
    
    for combi in sorted(list(combinations_with_replacement([i for i in range(11)], n)), key=lambda x: x[::-1]):
        lInfo = [0 for _ in range(11)]
        for i in combi:
            lInfo[i] += 1
        scoreGap = scoreCal(info, lInfo)
        if scoreGap <= 0: continue
        elif scoreGap >= maxScore:
            maxScore = scoreGap
            answer = lInfo
    
    return answer