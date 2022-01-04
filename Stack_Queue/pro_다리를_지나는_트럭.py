# 다리를 지나는 트럭
'''
<내 풀이>
  onBridge : 올라와 있는 트럭을 나타내는 stack
  - 가장 앞의 트럭이 나갈 시간이 되면 stack에서 pop한다.
  - 맨 앞의 트럭이 나가는 동시에 다른 트럭이 들어올 수도 있으므로, 
    맨 앞의 트럭이 완전히 나온 시간의 직전에 현재 pointing하는 트럭이 들어갈 수 있는지 검사한다.
'''
from collections import deque 

def solution(bridge_length, weight, truck_weights):
    # 첫번째 트럭 in
    i = 1
    time = 1
    onBridge = deque([(truck_weights[0], time + bridge_length)]) # 트럭 무게, 완전히 나올 시간
    weight -= truck_weights[0]
    
    # for 문 사용해도 되는데, stack 형식으로 풀려고 i 사용
    while i < len(truck_weights):
        # 맨 앞의 트럭이 나가는 중
        if time + 1 == onBridge[0][1]:
            outWeight, outTime = onBridge.popleft()
            weight += outWeight

        time += 1

        # 현재 트럭이 들어갈 수 있을 때
        if weight - truck_weights[i] >= 0:
            weight -= truck_weights[i]
            onBridge.append((truck_weights[i], time + bridge_length))
            i += 1
        
    # 마지막 트럭이 나가는 시간을 더한다.
    time += bridge_length
        
    return time

# 다른 사람 코드
'''
<다른 사람 풀이>
  - bridge : 다리의 칸 하나하나를 나타낸다.
  - 다리를 건널 수 있으면 해당 트럭의 무게를, 건널 수 없으면 0을 bridge에 push한다.
  - reverse한 이유는 list의 popleft 성능이 안좋아서 그럴 듯
'''
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse() 

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
'''