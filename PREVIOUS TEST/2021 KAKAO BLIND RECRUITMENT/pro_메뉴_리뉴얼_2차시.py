# 메뉴 리뉴얼
'''
<풀이 방법>
  - maxOrders[i] = 요리 i개로 구성된 코스요리 주문 수의 최댓값
  - course 각각에 orders에 지정한 개수의 combinations를 구한다.
'''
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    combis = defaultdict(int)
    maxOrders = [0] * 11
    
    for order in orders:
        for c in course:
            for combi in combinations(order, c):
                combis["".join(sorted(map(str, combi)))] += 1

    for combi in sorted(combis.items(), key = lambda x: x[1], reverse=True):
        if combi[1] >= maxOrders[len(combi[0])] and combi[1] >= 2:
            maxOrders[len(combi[0])] = combi[1]
            answer.append(combi[0])
    
    return sorted(answer)