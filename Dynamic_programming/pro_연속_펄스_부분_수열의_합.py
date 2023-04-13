# 연속 펄스 부분 수열의 합
'''
dp[i] = max(dp[i-1] + dp[i], dp[i])
'''

def solution(sequence):
    answer = 0
    pulseA = []
    pulseB = []
    
    now = -1
    for seq in sequence:
        pulseA.append(seq*now)
        now = -now
        pulseB.append(seq*now)
    
    for i in range(1, len(sequence)):
        pulseA[i] = max(pulseA[i-1] + pulseA[i], pulseA[i])
        pulseB[i] = max(pulseB[i-1] + pulseB[i], pulseB[i])
    
    return max(max(pulseA), max(pulseB))