# 분수 찾기
import sys

X = int(sys.stdin.readline().rstrip())

# X번째 분수는 i번째 대각선에 위치
i = 0

# 계차 수열(b_n = a_{n+1} - a_n) 이용
while X > 0:
    i += 1
    X -= i

# X번째 분수는 i번째 대각선의 remain번째에 위치
remain = X + i

# i가 홀수인 경우 분모가 늘어나고 분자 줄어드는 방향
if i % 2 == 1:
    print("%d/%d" %(i - remain + 1, remain))
else:
    print("%d/%d" %(remain, i - remain + 1))