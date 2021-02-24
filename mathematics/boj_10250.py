import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if ( N % H == 0 ):
        floor = H
        num = N // H
    else:
        floor = N % H
        num = N // H + 1
    # print( "%d0%d" %(floor, num) ) # 진짜 이거 때매 틀린거였으면 화나겠당^^
    print(floor*100 + num)