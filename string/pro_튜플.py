# 튜플
'''
<풀이 방법>
  - 나온 수를 dict에 카운트해서 넣고 answer에 append
'''
def solution(s):
    s = list(t.split(',') for t in s[2:-2].split('},{'))
    answer = [0 for _ in range(len(s))]
    cnt = {}
    
    for t in s:
        for e in t:
            if e not in cnt:
                cnt[e] = len(s)-1
            else: 
                cnt[e] -= 1
    
    for k, v in cnt.items():
        answer[v] = int(k)
    
    return answer

# 다른 사람 코드 1
'''
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
'''

# 다른 사람 코드 2
'''
<풀이 방법>
  - sort 후 배열에 없으면 append
'''
'''
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
'''