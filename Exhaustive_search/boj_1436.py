# 영화감독 숌

# 너무나도 허무한 다른 사람 코드 참고한 결과
# 때론 그냥 쉽게 생각하자..
# 참고 : https://pacific-ocean.tistory.com/137
import sys

N = int(sys.stdin.readline().rstrip())

count = 0
num = 666

while True:
    if '666' in str(num):
        count += 1
    if count == N:
        break
    num += 1

print(num)


# 아래 엄청 고민한 나의 흔적
'''
import sys

def factorial(N: int):
    if N <= 1:
        return 1
    return N * factorial(N-1)

N = int(sys.stdin.readline().rstrip())

digit = 3
num666 = 1

# digit자리수 중 666이 들어간 수의 갯수
# = 9 * 10**(digit-4) * (digit-3) + 10**(digit-3) - factorial(digit-3)
# ex) 5자리수 중 666이 들어간 수의 갯수 = 9*10*2 + 10**2 - 2!
while True:
    num666 += 9 * 10**(digit-4) * (digit-3) + 10**(digit-3) - factorial(digit-3)
    if N <= num666:
        break
    digit += 1
print(9 * 10**(digit-4) * (digit-3) + 10**(digit-3) - factorial(digit-3))
print(digit)

# digit자리수 중 666이 들어간 수 중 n_tmp 순서에 있는 것이 정답
# n_tmp = N
# num666 -= 9 * 10**(digit-4) * (digit-3) + 10**(digit-3) - factorial(digit-3)
# n_tmp -= num666

# num666_list = []
# for  in range(digit-3):



# for i in range(n_tmp):
'''