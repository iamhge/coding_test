# 직사각형으로 나누기
'''
행열 4파트로 쪼개는 것의 의미
ex)
123
456
789 의 경우

1|23
----
4|56
7|89
이런 식으로 쪼갠다.

위와 같이 쪼갠 사각형들 중 인접한 사각형 두개를 합치면 사각형 3개가 만들어진다.
ex)
123
----
4|56
7|89
'''
import sys

N, M = map(int, sys.stdin.readline().split())
rectangle = []
smallRec = []
result = 0

for _ in range(N):
    rectangle.append(list(map(int, list(sys.stdin.readline().rstrip()))))

# 세로로 나누는 경우
for i in range(1, M-1):
    for j in range(i+1, M):
        smallRec = [0]*3
        for k in range(N):
            smallRec[0] += sum(rectangle[k][:i])
            smallRec[1] += sum(rectangle[k][i:j])
            smallRec[2] += sum(rectangle[k][j:])
        result = max(smallRec[0]*smallRec[1]*smallRec[2], result)

# 가로로 나누는 경우
for i in range(1, N-1):
    for j in range(i+1, N):
        smallRec = [0]*3
        for k in range(N):
            if k < i:
                smallRec[0] += sum(rectangle[k])
            elif k < j:
                smallRec[1] += sum(rectangle[k])
            else:
                smallRec[2] += sum(rectangle[k])
        result = max(smallRec[0]*smallRec[1]*smallRec[2], result)

# 십자로 나누는 경우
for i in range(1, N): # 행
    for j in range(1, M): # 열
        smallRec = [0]*4 # 행열을 4파트로 쪼갠다.
        for _i in range(i): 
            smallRec[0] += sum(rectangle[_i][:j])
            smallRec[1] += sum(rectangle[_i][j:])
        for _i in range(i, N):
            smallRec[2] += sum(rectangle[_i][:j])
            smallRec[3] += sum(rectangle[_i][j:])
            
        # 4파트로 쪼갠 사각형 중, 인접한 두 직사각형을 하나로 합치며 비교
        result = max((smallRec[0]+smallRec[1])*smallRec[2]*smallRec[3]
                    , smallRec[0]*(smallRec[1]+smallRec[3])*smallRec[2]
                    , smallRec[0]*smallRec[1]*(smallRec[2]+smallRec[3])
                    , (smallRec[0]+smallRec[2])*smallRec[1]*smallRec[3]
                    , result)

print(result)
