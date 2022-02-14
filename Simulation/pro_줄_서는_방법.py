# 줄 서는 방법
'''
문제 풀이 실패
  사유) 런타임 에러를 못 고침
<풀이 방법>
  - 각 위치마다의 인덱스를 구하면서 줄을 세워간다.
  - k번째 방법의 i번째 사람의 번호는
    남은 사람들로 줄을 세우는 경우의 수 (n-i)! 중, k - (i-1번째 사람까지 세웠을 때의 경우의 수) 번째 이다.
    ex) k번째 방법에서 1번째 사람의 번호 = (k-1) // (n-1)! 번째 우선순위를 가지는 번호
  - priority : 우선순위로 나열된 남은 사람의 번호

런타임 에러 상황
  - n == 13
'''
import math

def solution(n, k): 
    answer = []
    priority = [i for i in range(1, n+1)]
    k -= 1
    for i in range(n-1, -1, -1):
        iFac = math.factorial(i)
        answer.append(priority[k//iFac])
        del priority[k//iFac]
        k = k % iFac
    return answer

# 시간 초과
'''
<풀이 방법>
  - 모든 경우의 수를 구한 후 정렬한다.
'''
'''
from itertools import permutations
def solution(n, k):
    return sorted(list(permutations([i for i in range(1, n+1)])))[k-1]
'''