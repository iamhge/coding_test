# 교점에 별 만들기
def solution(line): 
    answer = []
    n = len(line)
    intCross = set()
    
    for i in range(n):
        for j in range(i+1, n):
            A, B, E = line[i]
            C, D, F = line[j]
            
            if A*D == B*C:
                continue # 평행
            else:
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)
            
            if x // 1 == x and y // 1 == y: # x, y가 정수라면
                intCross.add((int(x), int(y)))
    
    maxX = max(intCross, key = lambda x: x[0])[0]
    minX = min(intCross, key = lambda x: x[0])[0]
    maxY = max(intCross, key = lambda x: x[1])[1]
    minY = min(intCross, key = lambda x: x[1])[1]
    
    array = [['.' for _ in range(maxX - minX + 1)] for _ in range(maxY - minY + 1)]
    for xy in intCross:
        array[maxY - xy[1]][xy[0] - minX] = '*'
    
    for row in array:
        answer.append("".join(row))
            
    return answer