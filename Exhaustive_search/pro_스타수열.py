# 스타 수열
# 다른 사람 풀이 참고
'''
<풀이 방법>
  1) a에 등장하는 원소 중 하나를 intersection number(in)로 가정한다.
  2) a를 순회하며 2개의 원소가 in을 포함하면 star 수열에 추가하고, index를 2 증가한다.
     단, 2개의 원소가 모두 in이면 star 수열에 넣지 않는다.
<개념 학습>
  Counter : 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 dictionary 객체를 얻게 된다.
<참고>
  프로그래머스 스타수열 (python, 파이썬) 
  : https://bladejun.tistory.com/119
  파이썬 collections 모듈의 Counter 사용법
  : https://www.daleseo.com/python-collections-counter/
  
ps. 알고나니 단순한데 왜 못풀었을까...
'''

from collections import Counter

def solution(a):
    answer = -1
    if len(a) == 1:
        return 0
    
    c = Counter(a)
    
    for k, v in c.items():
        # k의 값을 기준으로 스타수열을 만드는데
        # 2배가 최대의 max길이 배열인데 answer보다 작다면 진행할필요 x(시간초과 방지)
        if c[k]*2 < answer:
            continue
            
        idx = 0
        max_value = k
        length = 0
        while idx < len(a)-1:
            # idx랑 idx+1의 max_value의 값이 없으면 진행x
            # 둘의 값이 같다면 진행x
            if (a[idx] != max_value and a[idx+1] != max_value) or a[idx] == a[idx+1]:
                idx += 1
                continue
            
            # max_value를 포함하고 둘의 값이 같지 않다면
            # 조건을 만족하기 때문에 길이랑 idx랑 2씩 증가후 다음 배열 탐색
            length += 2
            idx += 2
        
        answer = max(answer, length)
        
    return answer

# 실패
'''
<풀이 방법>
  - intersection number가 3개 연속 붙어있을 경우 
 
'''
'''
from collections import defaultdict

def solution(a):
    answer = -1
    index = defaultdict(list)
    
    # index[x] = list(a 배열에서 x원소의 index)
    for i in range(len(a)):
        index[a[i]].append(i)
    
    # sorted(index, key = lambda x: -len(index[x])) : a 배열에서 가장 많이 등장하는 순서
    for intersectionNum in sorted(index, key = lambda x: -len(index[x])):
        indexTmp = index[intersectionNum]
        starLen = 0
        
        # nowPoint : 지금까지 부분 수열에 넣은 값의 a 배열에서 index
        if indexTmp[0] != 0:
            nowPoint = indexTmp[0]
        else:
            if indexTmp[1] == 1:
                
            nowPoint = min(indexTmp[], len(a))
            
        for i in range(1, len(indexTmp)):
            if indexTmp[i] - nowPoint >= 2:
                nowPoint = indexTmp[i]
                starLen += 2
        
        
        if indexTmp[0] == 0:
            for i in range(len(indexTmp)-1):
                if indexTmp[i+1] - indexTmp[i] > 1:
                    nowIndex = indexTmp[i] + 1
                    starLen += 2
        else:
            nowIndex = indexTmp[0]
            starLen += 2
            
            
            while indexTmp[i+1] - indexTmp[i] <= 1:
                i += 1
                
                nowIndex = indexTmp[i] + 1
                starLen += 2
        
        # [0, 0, 1, 0, 0, 1, 0]
                
        
        # for i in range(1, len(indexTmp)-1):
        #     if indexTmp[nowIndex]
            
            # if indexTmp[i] - nowIndex < 2 && indexTmp[i+1] - indexTmp[i] >= 2:
            #     nowPoint = 
            # elif indexTmp[i] - nowIndex >= 2 && indexTmp[i+1] - indexTmp[i] < 2:
            # elif indexTmp[i] - nowIndex < 2 && indexTmp[i+1] - indexTmp[i] < 2:
            # else:
            #     starLen += 2
                
                
        
        answer = max(answer, starLen)  
    return answer
'''
# 시간 초과
'''
<풀이 방법>
  - 모든 조합을 구하여, 스타 수열이 나올 경우 answer 을 업데이트 한다.
'''
'''
from itertools import combinations

def solution(a):
    answer = -1
    for n in range(len(a)//2+1):
        combis = list(combinations(a, n*2))
        for combi in combis:
            intersection = set(combi[:2])
            for i in range(n):
                # x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1]
                if combi[2*i] == combi[2*i+1]:
                    break
                    
                # 교집합의 원소의 개수가 1 이상
                intersection = intersection & set(combi[2*i:2*i+2])
                if len(intersection) < 1:
                    break
            else:
                answer = 2*n
        
    return answer
'''