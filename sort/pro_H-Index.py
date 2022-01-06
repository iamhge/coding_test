# H-Index

# h 보다 크거나 같은 수를 count
def countGTH(citations, h):
    count = 0
    for i in range(len(citations)):
        if citations[i] >= h:
            count = len(citations) - i
            break
    return count

def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(max(citations)+1):
        # h = i
        # h번 인용된 논문이 h 편 이상
        if countGTH(citations, i) >= i:
            answer = max(answer, i)
        else: break
    
    return answer
    
# 다른 사람 코드
'''
<다른 사람 풀이>
  - l - i == h == 몇 편이 남았는가
  - 내가 짠 코드는 h번 이상의 인용이 몇 편인가를 고려
    아래 코드는 몇 편이 남아있는가를 고려
'''
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

# 오답
'''
<오답 노트>
  - h가 citations의 원소가 아닐 수 있다.
<반례>
  ex) [1, 2, 2, 5, 6, 7] -> 3
'''
'''
def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations)):
        # h = citations[i]
        # h번 인용된 논문이 h편 이상
        if len(citations) - i >= citations[i]:
            answer = max(answer, citations[i])
    
    return answer
'''