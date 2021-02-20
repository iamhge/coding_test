# 리모컨
# 참고 : https://pacific-ocean.tistory.com/424
'''
5번이나 틀렸다.. 화난다..
'''
import sys

def checkNumNotInList(num: int, checkList: list):
    for j in list(str(num)):
        if j in checkList:
            return False
    return True

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
broken = []
if M > 0:
    broken = list(sys.stdin.readline().split())

# 이거 왜 틀린지 모르겠음;
# if M == 0:
#     print(len(str(N)))
# elif M == 10:
#     print(abs(N - 100))
# else:
result = abs(N - 100)

for i in range(1000001):
    if checkNumNotInList(i, broken):
        if abs(N - i) + len(str(i)) < result:
            result = abs(N - i) + len(str(i))

print(result)

# 틀린 방법
# 각 '자리수마다' 가장 가까운 숫자를 고른다.
# but 오류가 있음.
# 5457(broken : 5 7 8)의 경우 4446을 가장 가까운 숫자로 고르는데,
# 실제로 전체 수치로 가장 가까운 값은 4999이다.
'''
if M == 0:
    print(len(N))
elif M == 10:
    print(abs(n - 100))
else:
    remote = [str(i) for i in range(10)] 
    closestNum = ['' for _ in range(len(N))]
    for num in broken:
        remote.remove(num)

    for i in range(len(N)):
        mini = 10
        for r in remote:
            if abs(ord(r) - ord(N[i])) < mini:
                mini = abs(ord(r) - ord(N[i]))
                closestNum[i] = r
    print(closestNum)
    print(min(abs(int(''.join(closestNum)) - n) + len(N), abs(n - 100)))
'''