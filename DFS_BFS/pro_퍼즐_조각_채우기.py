# 퍼즐 조각 채우기
'''
<풀이 방법>
- 그냥.. 이게 맞나 싶었는데 맞는.. 완전탐색...
<오답 노트>
- getPuzzle에서 visited를 x, y에만 하고, nx, ny 탐색시에 바로 하지 않아 stack에 중복해서 들어가는 현상 발생.
  주의하자..!
<참고 링크>
프로그래머스 질문하기 란 중 1
: https://school.programmers.co.kr/questions/20288
<소감>
- 이전에 대기업 코테에서 정말 비슷한 문제가 나왔는데, 너무 난감했던 기억이 있다.
- 다시 풀어볼 수 있어서 다행이다.
'''
from collections import deque

dx = [1, -1, 0, 0] # 행
dy = [0, 0, 1, -1] # 열

# find인 부분을 찾아 list로 리턴한다. (find = 0 or 1)
# return 값: [puzzle, puzzle의 크기] 의 리스트
def getPuzzles(m, table, find):
    visited = [[False] * m for _ in range(m)]
    puzzles = []
    
    for i in range(m):
        for j in range(m):
            if not visited[i][j] and table[i][j] == find:
                puzzles.append(getPuzzle(m, table, (i, j), visited, find))
        
    return puzzles

def getPuzzle(m, table, start, visited, find): 
    stack = deque([start])
    puzzleCoordinate = [[start[0], start[1]]]
    visited[start[0]][start[1]] = True
    
    while stack:
        x, y = stack.pop()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < m and table[nx][ny] == find and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
                puzzleCoordinate.append([nx, ny])
    
    # puzzle의 x 좌표 시작 지점
    startX = min(puzzleCoordinate, key = lambda x: x[0])[0]
    # puzzle의 x 좌표 끝 지점
    endX = max(puzzleCoordinate, key = lambda x: x[0])[0]
    # puzzle의 y 좌표 시작 지점
    startY = min(puzzleCoordinate, key = lambda x: x[1])[1]
    # puzzle의 y 좌표 끝 지점
    endY = max(puzzleCoordinate, key = lambda x: x[1])[1]
    
    puzzle = [[0] * (endY-startY+1) for _ in range(endX-startX+1)]
    
    for x, y in puzzleCoordinate:
        puzzle[x-startX][y-startY] = 1
    
    return puzzle, len(puzzleCoordinate)

def turnPuzzle(puzzle):
    m = len(puzzle)
    n = len(puzzle[0])
    
    turned = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            if puzzle[i][j] == 1:
                turned[j][m-i-1] = 1
    
    return turned

def printPuzzle(puzzle):
    for p in puzzle:
        print(p)
    print()

def solution(game_board, table):
    answer = 0
    m = len(game_board)
    
    puzzles = getPuzzles(m, table, 1)
    empties = getPuzzles(m, game_board, 0)
    
    for puzzle, puzzleLen in puzzles:
        for _ in range(4):
            puzzle = turnPuzzle(puzzle)
            
            if (puzzle, puzzleLen) in empties:
                empties.remove((puzzle, puzzleLen))
                answer += puzzleLen
                break
    
    return answer