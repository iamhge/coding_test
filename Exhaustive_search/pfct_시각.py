# 시각
'''
3, 13, 23 , 30~39, 43, 53 분 -> 15가지
3, 13, 23 , 30~39, 43, 53 초 -> 15가지
3시, 13시, 23시의 경우 매순간이 포함된다. -> 60 * 60가지
'''
import sys

N = int(sys.stdin.readline())

# 분, 초에 3이 들어가는 경우의 수
ms = 15 * 60 * 2 - 15 * 15

# 시에 3이 들어가는 경우의 수
t = 60 * 60

if N >= 23:
    print(ms * (N - 2) + t * 3)
elif N >= 13:
    print(ms * (N - 1) + t * 2)
elif N >= 3:
    print(ms * N + t)
else:
    print(ms * (N + 1))

# 책 풀이 방법
'''
import sys

N = int(sys.stdin.readline())

count = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print (count)
'''