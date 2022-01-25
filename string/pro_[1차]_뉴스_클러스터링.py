# [1차] 뉴스 클러스터링
import re, math

def Jaccard(A, B):
    if len(A) == len(B) == 0:
        return 1
    
    intersection = 0 # 교집합
    for b in B:
        if b in A:
            A[A.index(b)] = ""
            intersection += 1
    union = len(A + B) - intersection # 합집합
    
    return intersection / union

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A = []
    B = []
    p = re.compile('[a-zA-Z]+[a-zA-Z]')
    
    for i in range(len(str1)-1):
        if p.match(str1[i:i+2]):
            A.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if p.match(str2[i:i+2]):
            B.append(str2[i:i+2])
    
    return math.floor(Jaccard(A, B) * 65536)

# 다른 사람 코드
'''
  - set을 사용해서 중복이 없는 교집합 gyo, 합집합 hap을 구한 후
    각 str1, str2에 대해 gyo, hap에 해당하는 원소의 개수를 sum한다.
'''
'''
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
'''