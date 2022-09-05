# 금과 은 운반하기
# 다른 사람 코드 참고
'''
<풀이 방법>
  - 이진 탐색(Binary search)
  - time을 기준으로 이진 탐색을 한다. 
<오답 노트>
  - gold와 silver를 각각 최대로 넣었을 때로 계산해야하는데 그렇게 안했었음.
  - 솔직히 개념 이해하기 너무 어려우니 아래에서 마지막 참고 url 읽는 게 나음.
<참고>
  - 프로그래머스 금과 은 운반하기 (python, 파이썬)
    : https://bladejun.tistory.com/166
  - [월간 코드 챌린지 시즌 3] 9월 문제 풀이
    : https://prgms.tistory.com/101
  - 프로그래머스 월간 챌린지 금과 은 운반하기 해설/코드 (파이썬)
    : https://whatryando.tistory.com/29
'''

def binarySearch(start, end, a, b, g, s, w, t):
    answer = end + 1
    
    while start <= end:
        gold = silver = 0
        mid = (start + end) // 2
        total = 0
        
        for i in range(len(g)):
            # totalW : i번째 트럭이 mid 시간동안 옮길 수 있는 총 무게
            # (mid + t[i]) // (2*t[i]) : 운반 횟수
            totalW = w[i] * ((mid + t[i]) // (2*t[i]))
            
            gold += min(g[i], totalW)
            silver += min(s[i], totalW)
            total += min(g[i] + s[i], totalW)
            
        if (gold >= a) and (silver >= b) and (total >= a + b):
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
            
    return answer

def solution(a, b, g, s, w, t):
    return binarySearch(0, (a+b) * 100000 * 2, a, b, g, s, w, t)

# 시간 초과 2
# 최대공약수
'''
def euclidean(n, m):
    while m % n != 0:
        remainder = m % n
        m = n
        n = remainder
    return n

def solution(a, b, g, s, w, t):
    answer = -1
    clk = 0
    gcdT = t[0]
    for i in range(1, len(t)):
        gcdT = euclidean(gcdT, t[i])
    
    while a > 0 or b > 0:
        clk += gcdT
        for i in range(len(g)):
            # 트럭이 신도시에 도착한 경우
            if clk % (2*t[i]) != 0 and clk % t[i] == 0:
                # 금
                gold = min(a, g[i], w[i])
                g[i] -= gold
                a -= gold
                # 은
                silver = min(b, s[i], w[i]-gold)
                s[i] -= silver
                b -= silver

    return clk
'''
# 시간 초과
'''
def solution(a, b, g, s, w, t):
    answer = -1
    clk = 0
    
    while a > 0 or b > 0:
        clk += 1
        for i in range(len(g)):
            # 트럭이 신도시에 도착한 경우
            if clk % (2*t[i]) != 0 and clk % t[i] == 0:
                # 금
                gold = min(a, g[i], w[i])
                g[i] -= gold
                a -= gold
                # 은
                silver = min(b, s[i], w[i]-gold)
                s[i] -= silver
                b -= silver
    
    return clk
'''