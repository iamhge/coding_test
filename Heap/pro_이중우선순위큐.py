# 이중우선순위큐
'''
<풀이 방법>
  - 단순 sort 후 최댓값, 최솟값 삭제
  - 마음에 들지 않는 풀이 방법. sort를 매번 해야해서 시간 효율성이 좋지 않다.
'''
def solution(operations):
    answer = []
    heap = []
    
    for op in operations:
        if op[0] == 'I':
            heap.append(int(op[2:]))
            heap.sort()
        else:
            if len(heap) <= 0: continue
            if op[2] == '1': # 최댓값 삭제
                del heap[-1]
            else: # 최솟값 삭제
                del heap[0]
    if heap == []: return [0, 0]
    return [heap[-1], heap[0]]

# 틀린 풀이
'''
<풀이 방법>
  - 최대 힙, 최소 힙을 따로 두어 관리
  - 힙의 길이가 0이 되면, 최대 힙 혹은 최소 힙에서 pop했을 때 엉뚱한 값이 pop 된다. 따라서 힙의 길이가 0이 되면 다시 []으로 초기화 시켜준다.
    ex) 최소 힙에서 모두 값을 빼서 힙의 길이가 0일 때, 최대 힙을 []으로 초기화 시켜주지 않으면 이후 힙에 값이 들어갔을 때 최대 힙에서는 이미 삭제된 값을 pop하게 된다.
<반례>
  - 채점에는 통과하나, 실제로는 틀린 코드이다.
  - ["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]
    기댓값 〉[3, 3]
    실행 결과 〉[3, 2]
'''
'''
import heapq

def solution(operations):
    maxh = []
    minh = []
    heapLen = 0
    
    for op in operations:
        if op[0] == 'I':
            heapq.heappush(maxh, (-int(op[2:]), int(op[2:])))
            heapq.heappush(minh, int(op[2:]))
            heapLen += 1
        else:
            if heapLen <= 0: continue
            if op[2] == '1': # 최댓값 삭제
                heapq.heappop(maxh)
            else: # 최솟값 삭제
                heapq.heappop(minh)
            heapLen -= 1
            if heapLen <= 0:
                maxh = []
                minh = []
    
    if heapLen <= 0: return [0, 0]
    return [maxh[0][1], minh[0]]
'''