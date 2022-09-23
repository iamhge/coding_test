# 통나무 자르기
# 해설 참고
'''
<풀이 방법>
  - 이분 탐색
  - 길이가 L인 통나무를 C번 잘랐을 때 나온 통나무들의 길이를 length 이하가 되게 한다.
    (-> 참고링크의 내용인데 이 문장을 보고 빡 이해가 갔음.)
<반례>
1)
10 4 2
1 4 5 10
ans: 5 1

2)
9 9 2
1 2 3 4 5 6 7 8 9
ans: 3 3

3)
5 3 4
4 1 1
ans: 3 1
<오답 노트>
  - 만약 가능한 것이 여러 가지라면, 처음 자르는 위치가 작은 것을 출력한다.
    위의 조건이 있기 때문에 C가 0이 아닐 경우 처음 자르는 위치가 더 작게 만들 수 있다.
<참고>
  [백준 / BOJ] 1114 통나무 자르기
  : https://dlwnsdud205.tistory.com/185
  반례 참고
  : https://www.acmicpc.net/board/view/96951
'''

import sys
input = sys.stdin.readline

def canCutLT(L, C, pieces, maxLen):
    if max(pieces) > maxLen: return -1 # 이거 필요한 이유 : 반례 3
    nowPieceLen = pieces[-1]
    end = L
    for i in range(len(pieces)-2, -1, -1):
        nextPieceLen = nowPieceLen + pieces[i]

        if nextPieceLen <= maxLen:
            nowPieceLen = nextPieceLen
        else:
            C -= 1
            end -= nowPieceLen
            nowPieceLen = pieces[i]
     
    if C < 0 or end > maxLen:
        return -1

    if C != 0:
        end = pieces[0]

    return end # 처음 자르는 위치

def binarySearch(L, K, C, cutLoc):
    cutLoc.sort()

    pieces = [cutLoc[0]]
    for k in range(1, K):
        pieces.append(cutLoc[k] - cutLoc[k-1])
    pieces.append(L-cutLoc[-1])
    start = 0
    end = L
    while start <= end:
        mid = (start + end) // 2
        result = canCutLT(L, C, pieces, mid)

        # mid를 최대 길이로 자르지 못할 때
        if result == -1:
            start = mid + 1
        # mid를 최대 길이로 자를 수 있을 때
        else:
            answer = [mid, result]
            end = mid - 1
    return answer

def main():
    # 통나무의 길이는 L이고, K개의 위치에서만 자를 수 있다. 자를 수 있는 횟수는 최대 C번
    L, K, C = map(int, input().split())
    cutLoc = list(map(int, input().split()))
    print(' '.join(map(str, binarySearch(L, K, C, cutLoc))))

main()

# 시간 초과 2
'''
import sys
input = sys.stdin.readline

def canCutLT(L, C, cutLoc, maxLen):
    end = L

    while C > 0 and end > maxLen:
        for i in range(end-maxLen, end):
            if i in cutLoc:
                end = i
                C -= 1
                break
        else:
            return -1
    
    if end > maxLen:
        return -1

    return end # 처음 자르는 위치

def binarySearch(L, K, C, cutLoc):
    start = 0
    end = L

    while start <= end:
        mid = (start + end) // 2
        result = canCutLT(L, C, cutLoc, mid)

        # mid를 최대 길이로 자르지 못할 때
        if result == -1:
            start = mid + 1
        # mid를 최대 길이로 자를 수 있을 때
        else:
            answer = [mid, result]
            end = mid - 1
    return answer

def main():
    # 통나무의 길이는 L이고, K개의 위치에서만 자를 수 있다. 자를 수 있는 횟수는 최대 C번
    L, K, C = map(int, input().split())
    cutLoc = list(map(int, input().split()))
    print(' '.join(map(str, binarySearch(L, K, C, cutLoc))))

main()
'''
# 시간 초과
'''
<풀이 방법>
  - 모든 경우의 수 탐색
'''
'''
import sys
from itertools import combinations

input = sys.stdin.readline

def solution(L, K, C, cutLoc):
    answer = []
    cutLoc.sort()
    C = min(K, C)
    cases = combinations(cutLoc, C)

    for case in cases:
        maxiParts = case[0]
        for i in range(1, C):
            maxiParts = max(maxiParts, case[i] - case[i-1])
        maxiParts = max(maxiParts, L - case[-1])
        answer.append([maxiParts, case[0]])
    return min(answer, key=lambda x: x[0])

def main():
    # 통나무의 길이는 L이고, K개의 위치에서만 자를 수 있다. 자를 수 있는 횟수는 최대 C번
    L, K, C = map(int, input().split())
    cutLoc = list(map(int, input().split()))
    print(' '.join(map(str, solution(L, K, C, cutLoc))))

main()
'''