# 내 코드
import sys

def getCanvas(N: int):
    canvas = [[]*N]*N

    if N == 3:
        return [["*", "*", "*"], ["*", " ", "*"], ["*", "*", "*"]]
    
    # N//3의 패턴을 canvas 전체에 채움
    patern = getCanvas(N//3)
    for i in range(3): 
        for j in range(N//3):
            canvas[(N//3)*i+j] = patern[j]*3
    
    # 가운데에 " "채움
    for i in range(N//3, (N//3)*2):
        for j in range(N//3, (N//3)*2):
            canvas[i][j] = " "

    return canvas

N = int(sys.stdin.readline().rstrip())

canvas = getCanvas(N)
for i in range(N):
    for j in range(N):
        print(canvas[i][j], end="")
    print("")

# 다른 사람 코드
