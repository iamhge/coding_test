# 110 옮기기
# 다른 사람 풀이 참고
'''
<풀이 방법>
  - '110'을 계속해서 추출한 다음, 한 번에 삽입한다.
  - 삽입 시 1의 앞, 0의 뒤에 삽입한다.
<참고 코드 및 해설>
  프로그래머스 110 옮기기 (python, 파이썬)
  : https://bladejun.tistory.com/153
  [프로그래머스] 110 옮기기(Python)
  : https://hkim-data.tistory.com/225
'''
def solution(s):
    answer = []
    
    for word in s:
        stack = []
        count = 0
        
        for char in word:
            if char == '0' and stack[-2:] == ['1', '1']:
                count += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(char)

        if count == 0:
            answer.append(word)
            continue
        
        string = ''
        while stack:
            if stack[-1] == '0':
                break
            else:
                string += stack.pop()
        
        answer.append(''.join(stack) + '110' * count + string[::-1])
        
    return answer

# 시간 초과
'''
<풀이 방법>
  - 사전 순으로, 0이 1을 우선한다.
  1) 문자열을 순회한다.
  2) '110'이 나오면, word가 사전 순으로 앞에 오는 위치에 '110'을 재삽입한다.
  3) 삽입한 위치의 뒤에서부터 다시 1)을 수행한다.
'''
'''
def solution(s):
    answer = []
    
    for originWord in s:
        word = originWord
        i = 0
        while i < len(word)-2:
            if word[i:i+3] != '110':
                i += 1
                continue
            changed = word[:i] + word[i+3:]
            
            for j in range(len(changed)):
                if changed[:j] + '110' + changed[j:] < word:
                    word = changed[:j] + '110' + changed[j:]
                    i = j + 3
            else:
                i += 1
            
        answer.append(word)
    return answer
'''