# 공유기 설치
'''
<아이디어>
  1. C-1구간으로 전체 구간을 나누어, 각 지점에서 앞뒤로 탐색하며 찾으려 함. -> 오답
  2. <참고> 란의 두번째 링크
      * 이분 탐색의 기준은 '공유기 사이의 거리'
      * 공유기 사이의 거리의 최솟값(min_gap)과 최댓값(max_gap)을 계산
      * gap = (max_gap + min_gap) // 2
<참고>
  백준 2110번 공유기 설치 문제 파이썬
   : https://kils-log-of-develop.tistory.com/204
  [ 파이썬][백준] 2110번: 공유기 설치
   : https://codingcocoon.tistory.com/165
'''
import sys

N, C = map(int, sys.stdin.readline().split())
house = []

for _ in range(N):
    house.append(int(sys.stdin.readline().rstrip()))

house.sort()
# 구글링하면 다 house[1] - house[0]으로 하는데 이상하긴 했음.
# 위처럼 했을 때의 반례) 5 3 / 1 7 8 9 10
min_gap = 1 
max_gap = house[N-1] - house[0]
result = 0

while min_gap <= max_gap:
    gap = (max_gap + min_gap) // 2

    cnt = 1 # house[0] 1개
    tmp = house[0]
    for i in range(1, N):
        if house[i] >= tmp + gap:
            tmp = house[i]
            cnt += 1
    if cnt >= C: # 크거나 같으면, gap을 증가시켜서 최대한 gap을 키운다.
        result = gap
        min_gap = gap + 1
    else: # 설치 가능한 공유기의 개수가 C보다 작으므로, gap을 감소
        max_gap = gap - 1

print(result)

'''
start = min(house)
end = max(house)
selectedHouse = {start, end}

while start <= end and C > 2:
    p = (end - start) // (C-1)
    print(start, p, end)
    
    if start+p in house:
        C -= 1
        selectedHouse.add(start+p)
    else:
        i = 1
        while (p - i > start) and (p + i < end):
            if start+p-i in house:
                C -= 1
                selectedHouse.add(start+(p-i))
                p -= i
                break
            elif start+p+i in house:
                C -= 1
                selectedHouse.add(start+(p+i))
                p += i
                break
            i += 1
    start += p + 1

shList = sorted(list(selectedHouse))
mini = 1000000000
print(shList)

for i in range(len(shList)-1):
    if mini > shList[i+1] - shList[i]:
        mini = shList[i+1] - shList[i]

print(mini)
'''