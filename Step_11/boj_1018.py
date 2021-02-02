# 체스판 다시 칠하기
import sys

N, M = map(int, sys.stdin.readline().split())
chess = [[]*M]*N

for i in range(N):
    chess[i] = list(sys.stdin.readline().rstrip())

minColoring = N*M

for i in range(N-7):
    for j in range(M-7):
        coloring = 0
        start = chess[i][j]
        for k in range(8): 
            for l in range(8):
                if (k + l)%2 == 0 and chess[i+k][j+l] != start:
                    coloring += 1
                elif (k + l)%2 == 1 and chess[i+k][j+l] == start:
                    coloring += 1
        # start를 바꾼 경우가 더 효율적일 수 있으므로 min적용
        if min(64 - coloring, coloring) < minColoring:
            minColoring = min(64 - coloring, coloring)

print(minColoring)

# 다른 사람 코드 cutter 참고(1차원 string list 자를 때 용이할 듯)
# 직전(prev) 색상과 current 색상 비교해서 판단 (내가 처음에 생각한 것)
'''
def cutter(org,n,m):
    # original의 n ~ n+8행 k
    # k행의 m:m+8 자름.
    return [k[m:m+8] for k in org[n:n+8]]

def check_wrong(cut):
    clr={'W':True,'B':False}
    prev=not (clr[cut[0][0]])
    wrong=0
    for line in cut:
        for color in line:
            if clr[color]==prev:
                wrong=wrong+1
            prev=not prev
        prev=not prev
    if(wrong>64-wrong):
        return (64-wrong)
    return wrong

n,m=map(int,input().split())
org=[]

for i in range(n):
    org.append(input())

mini=64

for a in range(n-7):
    for b in range(m-7):
        cut=cutter(org,a,b)
        print(cut)
        wr=check_wrong(cut)
        if wr<mini:
            mini=wr

print(mini)
'''