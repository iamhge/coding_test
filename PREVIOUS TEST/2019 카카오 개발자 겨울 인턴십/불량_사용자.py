# 불량 사용자
'''
<풀이 방법>
  - hashmap
  - product
'''
from collections import defaultdict
from itertools import combinations, product

def solution(user_id, banned_id):
    answer = 0
    hashmap = defaultdict(list)
    combisList = [[] for _ in range(9)] # combis[i] = 길이가 i인 user_id에서 *이 채워질 위치선정
    
    for i in range(1, 9):
        index = list(k for k in range(i))
        for j in range(i+1):
            combisList[i].extend( combinations(index, j) )
    
    for user in user_id:
        for combis in combisList[len(user)]:
            tmp = list(user)
            for c in combis:
                tmp[c] = '*'
            hashmap[''.join(tmp)].append(user)
    
    bannedList = [hashmap[banned] for banned in banned_id]
    bannedCases = list(product(*bannedList))
    
    casesSet = set()
    for case in bannedCases:
        caseSet = set(case)
        if len(caseSet) == len(banned_id):
            casesSet.add(tuple(sorted(caseSet)))

    return len(casesSet)

# 다른 사람 풀이
'''
<풀이 방법>
  - 굳이 해시맵 사용하지 않고, 하나하나 구함. 문자열의 길이가 길지 않아서 아래 방법도 괜찮다.
'''
'''
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)
'''