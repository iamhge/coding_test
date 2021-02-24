# 숫자 카드 2
'''
<개념>
  Binary Search(이분 탐색)
  * 시간 복잡도 : O(log N)
  * 정렬된 자료를 반으로 나누어 탐색하는 방법.
  * 자료는 오름차순으로 정렬된 자료여야 함.
<아이디어>
  1. 다 count -> 시간 초과
  2. 그냥 mid에서 target을 찾으면 mid + 1 ~ end / start ~ mid - 1을
     다시 binary search. -> 시간 초과
  3. mid에서 target을 찾으면 mid의 앞 뒤로 target인 card가 있을 것.
     So, mid의 앞 뒤로 1칸씩 이동하며 target을 count. -> 시간 초과
  4. 세어야 하는 개수가 여러개 인 것 + 찾아야하는 카드가 여러개 인 것 
     두가지 이유로 계속 시간초과 발생하여, cards를 한번 순회하며 갯수를
     count list에 저장하여 이후 찾아야하는 card에 대해서만 print -> 1000ms로 통과
<참고>
  강의노트 15-2. [탐색] 이진탐색(Binary Search) 알고리즘
   : https://wayhome25.github.io/cs/2017/04/15/cs-16/
<틀린 이유>
  all 시간 초과
'''
import sys

N = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().split()))

count = [0]*20000001

for card in cards:
    count[card] += 1

for card in search:
    print(count[card], end=" ")

# 다른 사람 코드
# Counter library 사용
'''
from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
m = int(input())
s_ = list(map(int, input().split()))
s = Counter(s)
for i in s_: print(s[i], end=" ")
'''

# 시간 초과 3
# 다른 사람들 코드 보면 비슷한 것 같은데 왜 난 초과되나..
'''
def Binary_search(target: int, data: list):
    cnt = 0
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            cnt += 1
            i = 1
            while mid-i >= start and data[mid-i] == target:
                cnt += 1
                i += 1
            i = 1
            while mid+i <= end and data[mid+i] == target:
                cnt += 1
                i += 1
            return cnt
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for card in search:
    print(Binary_search(card, cards), end=' ')
'''

# 시간 초과 2
'''
def Binary_search(target: int, start: int, end: int, data: list):
    cnt = 0

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            cnt += 1
            cnt += Binary_search(target, mid + 1, end, data)
            cnt += Binary_search(target, start, mid - 1, data)
            return cnt
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for card in search:
    print(Binary_search(card, 0, N-1, cards), end=' ')
'''

# 시간 초과 1
# 혹시나 했는데 시간 초과
'''
for card in search:
    print(cards.count(card), end=' ')
'''
