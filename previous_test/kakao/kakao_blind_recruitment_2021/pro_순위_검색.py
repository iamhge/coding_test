# 순위 검색 
'''
<풀이 방법>
  - 해시(Hash), 이진탐색(Binary Search)
  - binary search 직접 구현 -> binary search 라이브러리
<소감>
  - 정말 미친듯이 타이트한 효율성 테스트를 구현해야했다.
    보통 해시맵만 하거나, 이진탐색만 하거나인데, 둘 다 해야했다는 점에서 힘들었다.
  - 그리고 작은 것도 모두 효율성을 생각해야 했다..
  - 이진탐색도 이제 직접 구현보다는 라이브러리를 써야할 것 같다. 그게 더 효율성이 좋게 나온다.
<개념>
  [Python] bisect 사용법👀 / 이분탐색 / 코딩테스트
  - https://programming119.tistory.com/196
'''
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    infos = []
    hashmap = defaultdict(list)
    condition = [[0] * 5 for _ in range(len(query))]
    
    combis = []
    for i in range(5):
        combis.extend(list(combinations([0, 1, 2, 3], i)))
    
    for i in info:
        I = list(i.split())
        score = int(I[-1])
        for combi in combis:
            tmp = I[:-1]
            for c in combi:
                tmp[c] = '-'
            hashmap[''.join(tmp)].append(score)
        
    for k in hashmap:
        hashmap[k].sort()
    
    for q in query:
        nowQ = list(filter(lambda x: True if x != 'and' else False, q.split()))
        key = ''.join(nowQ[:-1])
        GTscoreIndex = bisect_left(hashmap[key], int(nowQ[-1]))
        # answer.append(len(hashmap[key][GTscoreIndex:])) # 이 코드 쓰면 효율성 테스트 두개 시간 초과 남..
        answer.append(len(hashmap[key]) - GTscoreIndex)
        
    return answer

# 시간 초과
'''
<풀이 방법>
  - Binary search (이진탐색)
<오답 노트>
  - 이진탐색이 안되는 줄 알았는데 모든 지원자의 점수가 조건보다 낮은 경우를 생각 못했음.
'''
'''
nowQ = []
infos = []

def conditionFilter(I):
    for i in range(4):
        if nowQ[i] != '-' and I[i] != nowQ[i]:
            return False
    return True

def binarySearch(target):
    # start, end, mid는 infos의 index
    global infos
    start = 0
    end = len(infos) - 1
    result = end + 1 # result를 이렇게 지정한 이유 : 모든 지원자의 점수가 조건보다 낮은 경우
    
    while start <= end:
        mid = (start + end) // 2
        nowScore = infos[mid][-1]
        
        if nowScore < target:
            start = mid + 1
        elif nowScore >= target:
            result = mid
            end = mid - 1
    
    return result

def solution(info, query):
    answer = []
    global nowQ
    global infos
    
    condition = [[0] * 5 for _ in range(len(query))]
    
    for i in info:
        I = list(i.split())
        I[-1] = int(I[-1])
        infos.append(I)
        
    infos.sort(key = lambda x: x[-1])
    
    for q in query:
        nowQ = list(filter(lambda x: True if x != 'and' else False, q.split()))
        GTscoreIndex = binarySearch(int(nowQ[-1]))
        # print(int(nowQ[-1]))
        # print(infos[GTscoreIndex:])
        GTscoreList = list(filter(conditionFilter, infos[GTscoreIndex:]))
        
        answer.append(len(GTscoreList))
        
    return answer
'''
# 시간 초과
'''
from collections import defaultdict


def solution(info, query):
    answer = [0] * len(query)
    global nowQ
    queries = []
    
    language = defaultdict(set)
    group = defaultdict(set)
    career = defaultdict(set)
    food = defaultdict(set)
    scores = []
    
    language['-'] = set(range(len(info)))
    group['-'] = set(range(len(info)))
    career['-'] = set(range(len(info)))
    food['-'] = set(range(len(info)))
    
    for i, information in enumerate(info):
        nowInfo = list(information.split())
        scores.append(nowInfo[-1])
        language[nowInfo[0]].add(i)
        group[nowInfo[1]].add(i)
        career[nowInfo[2]].add(i)
        food[nowInfo[3]].add(i)
    
    for i, q in enumerate(query):
        nowQ = list(filter(lambda x: True if x != 'and' else False, q.split()))
        for j in list(language[nowQ[0]] & group[nowQ[1]] & career[nowQ[2]] & food[nowQ[3]]):
            
            if int(scores[j]) >= int(nowQ[-1]):
                answer[i] += 1
    
    return answer
'''

# 시간 초과
'''
<개념 학습>
  - filter : 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져온다.
    참고 : https://dojang.io/mod/page/view.php?id=2360
  - lambda 함수는 if문과 else문이 함께 쓰여야한다. elif는 쓰일 수 없다.
'''

'''
nowQ = []

def conditionFilter(I):
    if int(nowQ[-1]) > int(I[-1]):
        return False
    for i in range(4):
        if nowQ[i] != '-' and I[i] != nowQ[i]:
            return False
    return True

def solution(info, query):
    answer = []
    global nowQ
    infos = []
    queries = []
    
    condition = [[0] * 5 for _ in range(len(query))]
    
    for i in info:
        infos.append(list(i.split()))
        
    for i, q in enumerate(query):
        nowQ = list(filter(lambda x: True if x != 'and' else False, q.split()))
        GTscore = list(filter(conditionFilter, infos))
        answer.append(len(GTscore))
        
    return answer
'''