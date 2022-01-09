# 구명보트
'''
<풀이 방법>
  - 구출되지 않은 사람 중, 가장 무거운 사람을 우선으로 태운다.
  - 가장 무거운 사람이 혼자 타거나, 타는 당시에 가장 가벼운 사람과 같이 탄다.
'''
def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    savedHeavy = 0
    savedLight = 0
    
    while savedHeavy + savedLight < n:
        heavy = people[n-savedHeavy-1]
        if people[savedLight] + heavy <= limit: # 같이 탐
            savedLight += 1
        savedHeavy += 1
        answer += 1
    
    return answer