# 호텔 방 배정
'''
다른 사람 코드 참고한 풀이
다시 풀어볼 것
<풀이 방법>
- 최적화된 Union-Find 알고리즘
<참고>
[알고리즘] Union-Find 알고리즘 (서로소 집합=Disjoint-Set)
: https://velog.io/@kimdukbae/Union-Find-알고리즘
'''
import sys
sys.setrecursionlimit(100000)


def find(rooms, room):
    if room not in rooms:
        # 시간 효율에 영향
        rooms[room] = room + 1
        return room
    
    # 경로 압축
    # find하며 만나는 모든 값의 부모 노드를 root로 만든다.
    rooms[room] = find(rooms, rooms[room])
    return rooms[room]

def solution(k, room_number):
    answer = []
    rooms = {} # 시간 효율에 영향

    for wantRoom in room_number:
        answer.append(find(rooms, wantRoom))
        
    return answer

# 효율성 일부 통과 불가
'''
<오답 노트>
- union-find를 쓰기는 했지만, rooms를 배열로 미리 모두 선언한 부분이 시간을 더 잡아먹은 것으로 보인다..
  더 줄이려면 rooms를 dict로 선언후, 방을 배정할 때 그 때 그 때 room을 추가한다.
'''
'''
import sys
sys.setrecursionlimit(100000)

def find(rooms, room):
    if rooms[room] == room:
        return room
    
    # 경로 압축
    # find하며 만나는 모든 값의 부모 노드를 root로 만든다.
    rooms[room] = find(rooms, rooms[room])
    return rooms[room]

def solution(k, room_number):
    answer = []
    rooms = [i for i in range(k+2)] # k방을 가져가면 rooms[k]가 k+1이라는 더미 방을 가리켜야하므로

    for wantRoom in room_number:
        getRoom = find(rooms, wantRoom)
        answer.append(getRoom)
        rooms[getRoom] = find(rooms, getRoom+1)
        
    return answer
'''


# 효율성 통과 불가
# binary search라 썼지만, 사실상은 아닌...그런...
'''
INF = 1000000000000

# 배정받을 방 번호 return
def binarySearch(start, end, rooms):
    mid = (start + end) // 2
    
    if start > end:
        return INF
    
    if mid not in rooms:
        return min(mid, binarySearch(start, mid-1, rooms))
    
    return min(binarySearch(start, mid-1, rooms), binarySearch(mid+1, end, rooms))
    
    return result

def solution(k, room_number):
    answer = []
    maxNum = 0
    
    for rm in room_number:
        if rm in answer:
            rm = binarySearch(rm, maxNum+1, answer)
        answer.append(rm)
        if rm > maxNum:
            maxNum = rm
        
    return answer
'''
# 당연하지만 호율성 테스트 모두 실패!
'''
def solution(k, room_number):
    answer = []
    maxNum = 0
    
    for rm in room_number:
        if rm in answer:
            while rm in answer:
                rm += 1
                
        answer.append(rm)
    
    return answer 
'''