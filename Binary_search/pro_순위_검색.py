# 순위 검색
# 효율성 테스트 통과 못함
'''
<풀이 방법>
  - score를 binary search로 찾는다.
  - 각 경우의 수에 대해 해시 알고리즘을 적용한다.
<참고>
  - [프로그래머스] 순위 검색 / 파이썬
    : https://velog.io/@dogcu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
'''
from itertools import product

LANG, PART, CAREER, FOOD, SCORE = 0, 1, 2, 3, 4

def GTscore(scores, score):
    start = 0
    end = len(scores) - 1
    mid = (start + end) // 2
    
    while start <= end:
        if scores[mid] < score:
            start = mid + 1
        elif scores[mid] >= score:
            if mid < 1: return len(scores) - mid
            elif scores[mid-1] < score: return len(scores) - mid
            end = mid - 1
        mid = (start + end) // 2
        
    return len(scores) - start

def solution(info, query):
    answer = []
    dictionary = {}
    queries = []
    
    for i in range(len(query)):
        queries.append(tuple(f for f in list(query[i].split(' ')) if f != 'and'))
        dictionary[queries[-1][:SCORE]] = []

    for i in range(len(info)):
        nowI = list(info[i].split())
        cases = list(product([nowI[LANG], '-'], [nowI[PART], '-'], [nowI[CAREER], '-'], [nowI[FOOD], '-']))
        for case in cases:
            if case in dictionary:
                dictionary[case].append(int(nowI[SCORE]))
        
    for q in queries:
        answer.append(GTscore(sorted(dictionary[q[:SCORE]]), int(q[SCORE])))
    
    return answer

# 시간 초과 5
'''
import re

SCORE_INDEX = 4

# 조건에 맞는 지원자 정보 리스트 반환
def find(infos, index, q):
    correct = []
    for i in infos:
        if i[index] == q:
            correct.append(i)
    return correct

def GTscore(infos, score):
    start = 0
    end = len(infos)-1
    mid = (start + end) // 2
    
    while start <= end:
        if int(infos[mid][SCORE_INDEX]) < score:
            start = mid + 1
        elif int(infos[mid][SCORE_INDEX]) >= score:
            if mid < 1: return mid
            elif int(infos[mid-1][SCORE_INDEX]) < score: return mid
            end = mid - 1
        mid = (start + end) // 2
        
    return start

def solution(info, query):
    answer = []
    infos = []
    
    info.sort(key=lambda x: int(re.sub(r'[^0-9]', '', x)))
    for i in range(len(info)):
        infos.append(list(info[i].split()))
        
    for i in range(len(query)):
        nowQ = [f for f in list(query[i].split(' ')) if f != 'and']
        nowCorrect = infos[GTscore(infos, int(nowQ[SCORE_INDEX])):]

        for j in range(4):
            if nowQ[j] == '-': continue
            nowCorrect = find(nowCorrect, j, nowQ[j])
        answer.append(len(nowCorrect))
    
    return answer
'''

# 시간 초과 4
'''
import re

form = [{"cpp": [], "java": [], "python": []}, 
        {"backend": [], "frontend": []}, 
        {"junior": [], "senior": []}, 
        {"chicken": [], "pizza": []}]

SCORE_INDEX = 4

def GTscore(infos, score):
    start = 0
    end = len(infos)-1
    mid = (start + end) // 2
    
    while start <= end:
        if int(infos[mid][SCORE_INDEX]) < score:
            start = mid + 1
        elif int(infos[mid][SCORE_INDEX]) >= score:
            if mid < 1: return mid
            elif int(infos[mid-1][SCORE_INDEX]) < score: return mid
            end = mid - 1
        mid = (start + end) // 2
        
    return start

def solution(info, query):
    answer = [0 for _ in range(len(query))]
    score = [0 for _ in range(len(info))]
    infos = []
    
    info.sort(key=lambda x: int(re.sub(r'[^0-9]', '', x)))

    for i in range(len(info)):
        infos.append(list(info[i].split()))
        for j in range(4):
            form[j][infos[i][j]].append(i)
        
    for i in range(len(query)):
        nowQ = [f for f in list(query[i].split(' ')) if f != 'and']
        nowCorrect = set(i for i in range(GTscore(infos, int(nowQ[SCORE_INDEX])), len(infos)))
        
        for j in range(4):
            if nowQ[j] == '-': continue
            nowCorrect &= set(form[j][nowQ[j]])
        answer[i] = len(nowCorrect)
    
    return answer

'''
# 시간 초과 3
'''
form = [{"cpp": [], "java": [], "python": []}, 
        {"backend": [], "frontend": []}, 
        {"junior": [], "senior": []}, 
        {"chicken": [], "pizza": []}]

SCORE_INDEX = 4

def solution(info, query):
    answer = [0 for _ in range(len(query))]
    score = [0 for _ in range(len(info))]
    for i in range(len(info)):
        nowI = list(info[i].split())
        for j in range(4):
            form[j][nowI[j]].append(i)
        score[i] = nowI[SCORE_INDEX]
    
    for i in range(len(query)):
        nowQ = [f for f in list(query[i].split(' ')) if f != 'and']
        nowCorrect = set(i for i in range(len(info)) if int(score[i]) >= int(nowQ[SCORE_INDEX]))
        for j in range(4):
            if nowQ[j] == '-': continue
            nowCorrect &= set(form[j][nowQ[j]])
        answer[i] = len(nowCorrect)
    
    return answer
'''

# 시간 초과 2
'''
import re

SCORE_INDEX = 4

def solution(info, query):
    answer = [0 for _ in range(len(query))]
    
    for i in range(len(query)):
        nowQ = [f for f in list(query[i].split(' ')) if f != 'and']
        for j in info:
            for k in range(4):
                if nowQ[k] == '-': continue
                if nowQ[k] not in j: break
            else:
                if int(nowQ[SCORE_INDEX]) <= int(re.sub(r'[^0-9]', '', j)):
                    answer[i] += 1
    
    return answer
'''

# 시간 초과 1
'''
form = [["cpp", "java", "python"], ["backend", "frontend"], ["junior", "senior"], ["chicken", "pizza"]]

SCORE_INDEX = 4

# 조건에 맞는 지원자 정보 리스트 반환
def find(infos, index, q):
    correct = []
    for i in infos:
        if i[index] == q:
            correct.append(i)
    return correct
def solution(info, query):
    answer = []
    infos = []
    queries = []
    
    for i in info:
        infos.append(list(i.split()))
        
    for q in query:
        queries.append([f for f in list(q.split(' ')) if f != 'and'])
    
    for q in queries:
        remain = [i for i in infos if int(i[SCORE_INDEX]) >= int(q[SCORE_INDEX])] # 조건에 맞는 지원자 정보 리스트
        for i in range(4):
            if q[i] == '-': continue
            remain = find(remain, i, q[i])
        answer.append(len(remain))
    
    return answer
'''