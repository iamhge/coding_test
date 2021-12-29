# 땅따먹기
def solution(land):
    N = len(land)
    M = len(land[0]) # 문제 상 4로 고정
    
    # a = 위 -> 아래 탐색 시 해당 칸에서 갖는 가장 큰 점수
    a = [[0 for _ in range(M)] for _ in range(N)]
    a[0] = land[0]
    
    for n in range(1, N):
        for m in range(M):
            for i in range(M):
                if i != m:
                    a[n][m] = max(a[n][m], land[n][m] + a[n-1][i])
    
    return max(a[N-1])