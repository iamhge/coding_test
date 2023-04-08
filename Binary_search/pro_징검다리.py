'''
<풀이 방법>
1) mid가 최솟값이 가능하면 탐색 범위를 높인다.
2) 불가능하면 탐색 범위를 낮춘다.
'''

def isPossible(between, target, n):
    i = 0
    while i < len(between):
        if between[i] < target:
            newBet = between[i]
            while newBet < target:
                if n <= 0 or i >= len(between)-1:
                    return False
                i += 1
                newBet += between[i]
                n -= 1
        i += 1
            
    return True

def binarySearch(start, end, between, n):
    mid = (start + end) // 2
    result = 0
    
    while start < end:
        if isPossible(between, mid, n):
            result = max(result, mid)
            start = mid + 1
        else:
            end = mid
        
        mid = (start + end) // 2
    
    return result

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    between = [rocks[0]]
    for i in range(1, len(rocks)):
        between.append(rocks[i] - rocks[i-1])
    between.append(distance-rocks[-1])
    
    return binarySearch(0, distance, between, n)