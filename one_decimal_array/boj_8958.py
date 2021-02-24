# OX퀴즈
import sys

N = int(sys.stdin.readline().rstrip())

# 기존 답변
'''
for _ in range(N):
    result = sys.stdin.readline().rstrip()
    score = 0
    score_temp = 1
    for i in range(len(result)): 
        if (result[i] == 'O'):
            score += score_temp
            if i == len(result) - 1: continue
            if (result[i + 1] == 'O'):
                score_temp += 1
            else:
                score_temp = 1

    print(score)
'''

# 다른 답변 참고
for _ in range(N):
    result = sys.stdin.readline().rstrip()
    score = 0
    score_temp = 0
    for elem in result:
        if (elem == 'O'):
            score_temp += 1
        else:
            score_temp = 0
        score += score_temp

    print(score)