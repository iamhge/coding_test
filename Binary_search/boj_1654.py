# 랜선 자르기
'''
<참고>
  #390 백준 파이썬 [1654] 랜선 자르기 - 이분탐색
   : https://claude-u.tistory.com/443
  백준 1654번(python)
   : https://hwiyong.tistory.com/384?category=844316
<틀린 이유>
  1. 런타임 에러 (NameError)
  2. 런타임 에러 (ZeroDivisionError)
  너무 많이 틀렸다.
  코드는 간단하지만 생각보다 생각해야 할 것이 많았던 문제.
'''
import sys

K, N = map(int, sys.stdin.readline().split())
LAN = []
for _ in range(K):
    LAN.append(int(sys.stdin.readline().rstrip()))

# 1로 하지 않고 0으로 하면 에러남
# ex) 1 3 / 5 입력시 ZeroDivisionError 발생
start = 1 
end = max(LAN)
result = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in LAN:
        cnt += i // mid

    # cnt == N이 없을 수 있다. 
    # 최대 길이로 잘라도, 최대 길이 이상의 남는 랜선이 생길 수 있기 때문.
    # 남는 랜선 길이가 꼭 최대 길이보다 작으란 법 없음.
    # ex) 2 4 / 24 / 38 -> 답) 12
    # cnt == N이어도 최대 길이가 나오지 않을 수 있으므로 계속 돌림.
    if cnt >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

# 틀린 코드
# 너무 복잡하고 이상하게 생각함.
# cnt == N인 경우를 무조건 찾아야한다고 생각함.
# but, cnt == N이 안되고 cnt > N 만 되는 경우도 있음.
'''
import sys

K, N = map(int, sys.stdin.readline().split())
LAN = []
for _ in range(K):
    LAN.append(int(sys.stdin.readline().rstrip()))

start = 0 
end = LAN[0]

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in LAN:
        cnt += i // mid

    if cnt = N:
        result = mid
        i = 1
        while mid + i <= end:
            cnt = 0
            for j in range(K):
                cnt += LAN[j] // (mid + i)
            if cnt != N:
                i -= 1
                break
            result = mid + i
            i += 1
        break
    elif cnt > N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
'''