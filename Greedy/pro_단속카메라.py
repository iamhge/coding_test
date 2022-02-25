# 단속카메라
'''
<풀이 방법>
  - 각 구간의 진출 지점을 기준으로 정렬한다.
  - 진입 지점이 마지막으로 설치된 카메라의 뒤에 있으면 겹치지 않는다는 의미이므로,
    해당 구간의 진출 지점에 카메라를 새로 설치한다.
<반례>
정렬하는 이유 ex)
[[2, 8], [6, 10], [7, 10], [8, 11], [10, 11], [0, 4]] -> 2
 -------
      -----
       ----
         --
----
-> 정렬하지 않으면 값이 제대로 나오지 않는다.
'''
def solution(routes):
    answer = 0
    # x[0]을 기준으로 정렬하면 틀린다.
    # 진입이 아닌 진출 지점에 카메라를 설치하기 때문
    routes.sort(key=lambda x: x[1])
    camera = -30001
    
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    
    return answer


# 맞지만 아름답지 않은 코드 
'''
<풀이 방법>
  - 겹치는 파트를 계속 검사한다.
  - 불필요한 코드가 많다.
'''
'''
def overlapLength(a, b):
    if b[0] <= a[0] <= b[1]:
        return b[1] - a[0]
    elif b[0] <= a[1] <= b[1]:
        return a[1] - b[0]
    return -1

def overlap(a, b):
    if a[0] <= b[0]:
        start = b[0]
    else:
        start = a[0]
        
    if a[1] <= b[1]:
        end = a[1]
    else:
        end = b[1]
    return [start, end]

def solution(routes):
    routes.sort(key=lambda x: x[0])
    sections = [sorted(routes[0])]
                
    for route in routes:
        ol = -1
        addSection = route
        deleteSection = None
        for section in sections:
            oltmp = overlapLength(sorted(route), section)
            if ol < oltmp:
                ol = oltmp
                addSection = overlap(route, section)
                deleteSection = section
        if deleteSection != None:
            sections.remove(deleteSection)
            
        sections.append(addSection)
    
    return len(sections)
'''