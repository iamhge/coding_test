# N 찍기
import sys

# N = int(sys.stdin.readline().rstrip())
# for i in range(N):
#     print(i + 1)

N = range(1, int(sys.stdin.readline().rstrip()) + 1)
# ''.join(list) : str list 사이에 ''를 껴서 str로 변환
print( '\n'.join(map(str, N)))