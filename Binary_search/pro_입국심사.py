# 입국심사
'''
<풀이 방법>
  이분탐색
  - 이분탐색 할 대상 : 모든 사람이 심사를 받는데 걸리는 시간
  - possibleTime(n, totalTime, times)
    : totalTime 동안 모든 사람의 입국 심사를 할 수 있는가 검사한다.
      입국심사관이 모두 쉼없이 검사했을 때 totalTime 안에 검사가 가능한지 확인한다.
'''
def possibleTime(n, totalTime, times):
    for time in times:
        n -= totalTime // time
    if n > 0:
        return False
    return True
    

def solution(n, times):
    answer = 0
    times.sort(reverse = True)
    start = 1
    end = 1000000000 * 1000000000
    
    while start <= end:
        mid = (start + end) // 2
        
        if possibleTime(n, mid, times):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer