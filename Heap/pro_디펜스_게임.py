# 디펜스 게임
import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    answer = k
    sumIround = sum(enemy[:k]) # i round까지의 전체 enemy 수
    invincibility = sumIround # 무적권을 사용한 round의 enemy 수
    invinEnemy = sorted(enemy[:k][::]) # 무적권을 사용한 round의 enemy들
    heapq.heapify(invinEnemy) # 최소 힙
    
    for i in range(k, len(enemy)):
        sumIround += enemy[i]
        
        if enemy[i] > invinEnemy[0]:
            invincibility += enemy[i] - heapq.heappop(invinEnemy)
            heapq.heappush(invinEnemy, enemy[i])
        
        if n >= sumIround - invincibility:
            answer = i+1
        else:
            break
    
    return answer