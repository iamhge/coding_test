# 메뉴 리뉴얼
from itertools import combinations

def solution(orders, course):
    candidates = [{} for _ in range(max(course)+1)]
    answer = []
    
    for order in orders:
        for i in course:
            if i > len(order): break
            combis = list(combinations(sorted(list(order)), i))
            for combi in combis:
                if combi not in candidates[i]:
                    candidates[i][combi] = 0
                candidates[i][combi] += 1
    
    for i in course:
        if len(candidates[i]) == 0: continue
        maxN = max(list(candidates[i].values()))
        if maxN < 2: continue
        for c in candidates[i]:
            if candidates[i][c] == maxN:
                answer.append(''.join(c))
        
    return sorted(answer)

# 다른 사람 풀이
'''
<풀이 방법>
  - Counter를 이용한 풀이
<참고>
  - [파이썬] collections 모듈의 Counter 클래스 사용법
    : https://www.daleseo.com/python-collections-counter/
'''
'''
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

'''