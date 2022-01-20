# 삼각 달팽이
'''
<풀이 방법>
  - 남 -> 동 -> 북서 방향으로 계속 값이 갱신된다.
  - 2차원 배열에 채운 후 합쳐 return
'''
def solution(n):
    answer = []
    array = [[0 for _ in range(n)] for _ in range(n)]
    now = 1
    row = -1
    col = 0
    
    for turn in range(n):
        for _ in range(turn, n):
            if turn % 3 == 0: # 남
                row += 1
            elif turn % 3 == 1: # 동
                col += 1
            else: # 북서
                row -= 1
                col -= 1
            array[row][col] = now
            now += 1
    
    for i in range(n):
        answer.extend(array[i][:i+1])
        
    return answer

# 시간 초과
'''
length를 잘못구했긴했는데, 위에랑 무슨 차인지 모르겠다.

5 / 4 / 3 / 2 / 1
00 10 20 30 40 / 41 42 43 44 / 33 22 11 / 21 31 / 32
남 / 동 / 북서 / 남 / 동

6 / 5 / 4 / 3 / 2 / 1
00 10 20 30 40 50 / 51 52 53 54 55 / 44 33 22 11 / 21 31 41 / 42 43 / 32
남 / 동 / 북서 / 남 / 동 / 북서
'''
'''
def solution(n):
    answer = []
    length = n * (1 + n) // 2
    array = [[0 for _ in range(length)] for _ in range(length)]
    tmp = n
    now = 1
    turn = 1
    row = -1
    col = 0
    
    while tmp >= 1:
        for i in range(tmp):
            if turn % 3 == 1: # 남
                row += 1
            elif turn % 3 == 2: # 동
                col += 1
            else: # 북서
                row -= 1
                col -= 1
            array[row][col] = now
            now += 1
        
        tmp -= 1
        turn += 1
    
    for i in range(n):
        answer.extend(array[i][:i+1])
        
    return answer
'''