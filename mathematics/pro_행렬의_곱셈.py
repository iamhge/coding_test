# 행렬의 곱셈
def solution(arr1, arr2):
    # arr1 = N X M 행렬, arr2 = M X L 행렬
    N = len(arr1)
    M = len(arr1[0])
    L = len(arr2[0])
    answer = [[0 for _ in range(L)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            for k in range(L):
                answer[i][k] += arr1[i][j] * arr2[j][k]
    
    return answer

# 정답이지만 코딩 테스트에서는 numpy 사용 불가가 많음.
'''
import numpy as np

def solution(arr1, arr2):
    answer = np.array(arr1).dot(np.array(arr2)).tolist()
    return answer
'''