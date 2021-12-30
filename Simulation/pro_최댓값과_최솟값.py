# 최댓값과 최솟값
def solution(s):
    l = list(map(int, s.split()))
    answer = str(min(l)) + ' ' + str(max(l))
    return answer