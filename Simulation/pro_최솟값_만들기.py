# 최솟값 만들기
'''
<개념>
  각 배열에서 가장 작은 수, 가장 큰 수끼리 곱해야 최종적으로 최소가 될 것
'''
def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer