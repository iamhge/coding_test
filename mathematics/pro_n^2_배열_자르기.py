# n^2 배열 자르기
'''
<풀이 방법>
  - i % n -> 2차원 배열의 열
  - i // n -> 2차원 배열의 행
  - max(i % n, i // n) + 1 -> 2차원 배열의 해당 칸의 값
'''
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i % n, i // n) + 1)
    return answer

# 시간 초과
'''
def solution(n, left, right):
    # 1
    array = [[0 for _ in range(n)] for _ in range(n)]
    
    # 2
    for i in range(n):
        for j in range(n):
            array[i][j] = max(i, j) + 1
    
    # 3
    answer = []
    for a in array:
        answer.extend(a)
    
    # 4
    return answer[left:right+1]
'''