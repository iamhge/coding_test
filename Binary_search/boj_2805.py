# 나무 자르기
'''
<틀린 이유>
  3번 all 시간초과..
  똑같은 알고리즘으로 pypy3으로 제출하니 맞았다.
'''
import sys

N, M = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(height)
result = 0

while start <= end:
    mid = (start + end) // 2
    wood = 0

    for h in height:
        if h > mid:
            wood += h - mid

    # wood == M이 아닌 경우도 최대 높이 일 수 있다.
    # ex) 4 7 / 20 15 10 18 -> 답) 15
    #     16으로 자르면 6만 가져갈 수 있고, 15로 자르면 8을 가져감.
    #     so, wood == M일 수 없으므로 15가 최적값
    if wood > M: # 덜 잘라야 함.
        result = mid
        start = mid + 1
    elif wood == M: # 랜선 자르기(boj_1654)와 달리 wood == M이면 최적임.
        result = mid
        break
    else: # 더 잘라야 함.
        end = mid - 1

print(result)