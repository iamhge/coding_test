# 당구 연습
'''
<풀이 방법>
- 반사할 때 하나의 공이 벽 너머로 반전된다고 생각하고 거리 구하면 됨.
  ex) 왼쪽 벽: (startX + x)**2 + (y좌표 차)**2
'''

INF = 2000000000001

def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        distSq = INF
        x, y = map(int, ball)
        xDist = abs(startX - x)
        yDist = abs(startY - y)
        
        # 좌
        if not (startY == y and startX > x):
            distSq = min(distSq, ((startX + x)**2 + yDist**2))
        # 우
        if not (startY == y and startX < x):
            distSq = min(distSq, ((2*m - startX - x)**2 + yDist**2))
        # 상
        if not (startX == x and startY < y):
            distSq = min(distSq, ((2*n - startY - y)**2 + xDist**2))
        # 하
        if not (startX == x and startY > y):
            distSq = min(distSq, ((startY + y)**2 + xDist**2))
        
        answer.append(distSq)
    
    return answer