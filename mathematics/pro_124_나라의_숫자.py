# 124 나라의 숫자
# Level 2
# 연습문제
'''
11 -> 42
12 -> 44
13 -> 111
14 -> 112
15 -> 114
16 -> 121
17 -> 122
18 -> 124
3
3+9
3+9+27
'''
def solution(n):
    answer = ''
    
    while n > 0:
        if n%3 == 0:
            # 마지막 자리가 4
            answer = '4' + answer
        elif n%3 == 1:
            # 마지막 자리가 1
            answer = '1' + answer
        else:
            # 마지막 자리가 2
            answer = '2' + answer
        n = (n-1) // 3

    return answer