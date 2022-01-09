# 조이스틱
'''
<풀이 방법>
  - Greedy로 푼다.
  - 그 때 그 때 알파벳을 setting한 후, answer에 해당 count를 더하고 나면 
    이후는 그 자리가 'A'인 것으로 친다.
  - i = 현재 인덱스
  - j = 'A'가 나오지 않을 때 까지 뒤로 이동하는 수
  - k = 'A'가 나오지 않을 때 까지 앞으로 이동하는 수
  - j와 k 중 더 짧게 이동하는 쪽으로 이동한다.
  - j와 k가 같은 경우는 어떻게 고려해야할지 모르겠다.
<반례>
  ex) "ABBAAAAAAAAAB" -> 7
<내 생각>
  - Greedy로 풀긴했지만 왜 Greedy인지 모르겠다. 그냥 짬뽕문제 같다. 이상한 문제다.
'''
def solution(name):
    n = len(name)
    count = [min(ord(c)-ord('A'), 1+ord('Z')-ord(c)) for c in name]
    answer = 0
    i = 0
    
    # 시작 자리 설정
    answer += count[i]
    count[i] = 0
    
    while count.count(0) < n:
        j = 1 # 'A'가 나오지 않을 때 까지 뒤로 이동하는 수
        while count[i-j] == 0: # 뒤로 계속 'A'가 있는 경우
            j += 1
        
        k = 1 # 'A'가 나오지 않을 때 까지 앞으로 이동하는 수
        while count[(i+k)%n] == 0: # 앞으로 계속 'A'가 있는 경우
            k += 1
        
        if j < k:
            answer += j
            i -= j
        elif k < j:
            answer += k
            i = (i+k)%n
        else: # k == j
            # 모르겠다...
        
        answer += count[i]
        count[i] = 0 # 바꾼 자리를 'A'로 set
    
    return answer

# 틀린 코드 1
'''
<오답 노트>
  - 앞으로 갔다가 뒤로가는 경우를 고려하지 않음
  - A가 연달아 있는 경우를 고려하지 않음
<반례>
  - ex) "ABAAAAAAAAABB" -> 7
'''
'''
def solution(name):
    count = [min(ord(c)-ord('A'), 1+ord('Z')-ord(c)) for c in name]
    
    if name[-1] == 'A' or name[1] == 'A':
        return sum(count) + len(name) - 2
    else:
        return sum(count) + len(name) - 1
'''

# 틀린 코드 2
'''
<오답 노트>
  - <'A'가 나오지 않을 때 까지 뒤로 이동하는 수 == 'A'가 나오지 않을 때 까지 앞으로 이동하는 수> 일 때의 처리가 틀림
    해당 경우, 뒤로갔을 때와 앞으로 갔을 때 모두를 고려해주어야 한다.
<반례>
  ex) "ABAAAAAAAAABB" -> 7
'''
'''
def solution(name):
    n = len(name)
    count = [min(ord(c)-ord('A'), 1+ord('Z')-ord(c)) for c in name]
    answer = 0
    i = 0
    
    # 시작 자리 설정
    answer += count[i]
    count[i] = 0
    
    while count.count(0) < n:
        j = 1 # 'A'가 나오지 않을 때 까지 뒤로 이동하는 수
        while count[i-j] == 0: # 뒤로 계속 'A'가 있는 경우
            j += 1
        
        k = 1 # 'A'가 나오지 않을 때 까지 앞으로 이동하는 수
        while count[(i+k)%n] == 0: # 앞으로 계속 'A'가 있는 경우
            k += 1
        
        if j <= k: # 여기에서 틀림
            answer += j
            i -= j
        else:
            answer += k
            i = (i+k)%n
        
        answer += count[i]
        count[i] = 0 # 바꾼 자리를 'A'로 set
    
    return answer
'''

# 틀린 코드 3
'''
<오답 노트>
  - 틀린 코드 2와 같다. 하지만 실제로 프로그래머스에 제출 후 채점하면 정답이라고 나온다.
  - 하지만 다음의 반례에 의해 틀린 코드이다.
<반례>
  ex) "ABBAAAAAAAAAB" -> 7
'''
'''
def solution(name):
    n = len(name)
    count = [min(ord(c)-ord('A'), 1+ord('Z')-ord(c)) for c in name]
    answer = 0
    i = 0
    
    # 시작 자리 설정
    answer += count[i]
    count[i] = 0
    
    while count.count(0) < n:
        j = 1 # 'A'가 나오지 않을 때 까지 뒤로 이동하는 수
        while count[i-j] == 0: # 뒤로 계속 'A'가 있는 경우
            j += 1
        
        k = 1 # 'A'가 나오지 않을 때 까지 앞으로 이동하는 수
        while count[(i+k)%n] == 0: # 앞으로 계속 'A'가 있는 경우
            k += 1
        
        if j < k:
            answer += j
            i -= j
        else:
            answer += k
            i = (i+k)%n
        
        answer += count[i]
        count[i] = 0 # 바꾼 자리를 'A'로 set
    
    return answer
'''