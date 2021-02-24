# 덩치
import sys

N = int(sys.stdin.readline().rstrip())
rank = [1] * N
bulk = []

for _ in range(N):
    bulk.append( tuple( map(int, sys.stdin.readline().split()) ) )

for i in range(N):
    for j in range(N):
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            rank[i] += 1

for r in rank:
    print(r, end=" ")

# Q. 둘중 하나는 같고 나머지 하나는 다른 사람은..?
# A. 문제에 둘다 커야 덩치큰거라고 나와있음.
#    내가 문제 제대로 안읽고 복잡하다고 혼자 난리피움ㅡㅡ짱난당

# 기수정렬(Radix Sort)은 기수간 우선순위가 있기에 적합하지 않다고 함
# 참고 : https://claude-u.tistory.com/122 
''' 틀린 코드
for _ in range(N):
    bulk.append( tuple( map(int, sys.stdin.readline().split()) ) )

    for i in range( len(bulk) - 1 ):
        x_diff = bulk[-1][0] - bulk[i][0]
        y_diff = bulk[-1][1] - bulk[i][1]
        
        if (x_diff * y_diff < 0) or (x_diff == 0 and y_diff == 0):
            rank[len(bulk)-1] -= 1
            rank[i] -= 1
        elif x_diff * y_diff > 0:
            if x_diff > 0: 
                rank[len(bulk)-1] -= 1
            else:
                rank[i] -= 1
        else:
            if x_diff > 0: 
                rank[len(bulk)-1] -= 1
            else:
                rank[i] -= 1
'''

