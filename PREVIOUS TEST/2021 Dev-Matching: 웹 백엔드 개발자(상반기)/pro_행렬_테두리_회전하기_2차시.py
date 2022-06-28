# 행렬 테두리 회전하기 2차시
# 2차시
'''
x1, y1 / x1, y2
x2, y1 / x2, y2
'''

def turnMatrix(x1, y1, x2, y2, matrix):
    minNum = len(matrix) * len(matrix[0])
    tmp = matrix[x2][y1]
    
    # 아랫 면 - 오른쪽에 있는 숫자를 왼쪽에 옮긴다.
    for ny in range(y1, y2):
        minNum = min(minNum, matrix[x2][ny])
        matrix[x2][ny] = matrix[x2][ny + 1]
    
    # 오른쪽 면 - 위에 있는 숫자를 아래로 옮긴다.
    for nx in range(x2, x1, -1):
        minNum = min(minNum, matrix[nx][y2])
        matrix[nx][y2] = matrix[nx - 1][y2]
        
    # 윗 면 - 왼쪽에 있는 숫자를 오른쪽으로 옮긴다.
    for ny in range(y2, y1, -1):
        minNum = min(minNum, matrix[x1][ny])
        matrix[x1][ny] = matrix[x1][ny - 1]
    
    # 왼쪽 면 - 아래에 있는 숫자를 위로 옮긴다.
    for nx in range(x1, x2):
        minNum = min(minNum, matrix[nx][y1])
        matrix[nx][y1] = matrix[nx + 1][y1]
    
    matrix[x2 - 1][y1] = tmp
    
    return minNum
    

def solution(rows, columns, queries):
    answer = []
    matrix = [[i + j*columns for i in range(1, columns+1)] for j in range(rows)]
    
    for query in queries:
        answer.append(turnMatrix(query[0]-1, query[1]-1, query[2]-1, query[3]-1, matrix))
    
    return answer