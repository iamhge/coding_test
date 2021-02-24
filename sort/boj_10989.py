# 수 정렬하기 3
# 정렬하지 않고 정렬한 효과를 낼 수 있음.
# 이 문제에서 메모리 초과가 나는 이유 : 
# 이 문제는 수 정렬하기 1, 2와 달라서
# N개의 수를 모두 append후 sort하면, 10000보다 작은 수만 입력받아도 수가 반복 입력될 수 있음.
# 예를 들어 1, 1, 1, 3, 3, 3, ... 식으로 같은 수가 반복되어 입력될 수 있으므로,
# 입력받아야하는 수의 개수(N)가 최대인 10000000이면 아래와 같이 원소 10000개를 갖는 list보다
# 메모리를 더 잡아 먹게 됨.
import sys

N = int(sys.stdin.readline().rstrip())
numList = [0] * 10001

for _ in range(N):
    numList[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(numList)):
    while numList[i] != 0:
        numList[i] -= 1
        print(i)