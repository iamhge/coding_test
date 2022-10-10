# 행렬 테두리 회전하기
# 하 우 상 좌 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def pM(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()

def solution(rows, columns, queries):
    answer = []
    matrix = [[i+columns*j for i in range(1, columns+1)] for j in range(rows)]
    
    for query in queries:
        y1, x1, y2, x2 = (xy-1 for xy in query)
        nx, ny = x1, y1
        start = matrix[ny][nx]
        i = 0
        mini = rows*columns
        while True:
            mini = min(mini, matrix[ny][nx])
            matrix[ny][nx] = matrix[ny+dy[i]][nx+dx[i]]
            if (nx+dx[i], ny+dy[i]) == (x1, y1): break
            nx += dx[i]
            ny += dy[i]
            if (nx, ny) == (x1, y1) or (nx, ny) == (x1, y2) or (nx, ny) == (x2, y1) or (nx, ny) == (x2, y2): # 방향 전환
                i += 1
            
        matrix[ny][nx] = start
        answer.append(mini)
    return answer