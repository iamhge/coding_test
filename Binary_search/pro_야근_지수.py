# 야근 지수
'''
<풀이 방법>
  이분 탐색
  - boj_2805.py(백준 2805 - 나무 자르기)를 풀었던 아이디어를 활용했다.
  - 이분 탐색을 통해 (남은 작업량들의 최댓값)의 최솟값을 구한다.
    예를 들어 남은 작업량의 배열이 [1, 2, 3, 3] 이라 했을 때, (남은 작업량들의 최댓값) = 3이고, 
    이분 탐색을 통해 이 값을 최소로 하는 것을 목표한다.
'''

def working(mid, works):
    time = 0 # 작업 시간
    for work in works:
        if work > mid:
            time += work - mid
    return time

def binarySearch(start, end, works, n):
    result = end, 0
    while start < end:
        mid = (start + end) // 2
        time = working(mid, works)
        if time <= n:
            result = mid, time
            end = mid
        else:
            start = mid + 1
    return result

def solution(n, works):
    answer = 0
    if sum(works) <= n: return 0

    works.sort()
    mid, time = binarySearch(0, works[-1], works, n)
    remainTime = n - time

    for i in range(len(works) - remainTime):
        if works[i] > mid:
            answer += mid**2
        else:
            answer += works[i]**2
    
    answer += (mid-1)**2 * remainTime
        
    return answer

# 시간 초과
'''
<풀이 방법>
  - works의 가장 큰 수를 1씩 n번 뺀다.
'''
'''
def solution(n, works):
    answer = 0
    while n > 0:
        works.sort()
        if works[-1] == 0: break
        works[-1] -= 1
        n -= 1
    for work in works:
        answer += work**2
    return answer
'''

# 다른 사람 풀이
'''
import heapq
def solution(n, works):
    answer = 0
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, (-work, work))

    for i in range(n):
        work = heapq.heappop(max_heap)
        if work[1] == 0:
            break
        heapq.heappush(max_heap, (-work[1] + 1, work[1] - 1))

    for i in range(len(max_heap)):
        answer += max_heap[i][1] ** 2

    return answer
'''