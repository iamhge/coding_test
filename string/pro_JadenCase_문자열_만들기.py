# JadenCase 문자열 만들기
'''
<오답 이유>
  앞과 뒤에 공백이 있는 경우의 수를 간과했음.
  ex) "  aa bb  cc " -> ""  Aa Bb  Cc ""
'''

def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z' and (i == 0 or s[i-1] == ' '):
            answer += s[i].upper()
        elif 'A' <= s[i] <= 'Z' and (i != 0 and s[i-1] != ' '):
            answer += s[i].lower()
        else:
            answer += s[i]
    
    return answer


# 실패
'''
def solution(s):
    answer = ''
    strList = s.split()
    
    for i in range(len(strList)):
        strList[i] = strList[i].capitalize()
    answer = ' '.join(strList)

    return answer
'''
'''
def solution(s):
    answer = ''
    strList = s.split()
    
    for word in strList:
        answer += word.capitalize() + ' '

    return answer[:-1]
'''
'''
def solution(s):
    answer = ''
    strList = s.split()
    
    for word in strList:
        for i in range(len(word)):
            if 'a' <= word[i] <= 'z' and i == 0:
                answer += word[i].upper()
            elif 'A' <= word[i] <= 'Z' and i != 0:
                answer += word[i].lower()
            else:
                answer += word[i]
        answer += ' '
    
    return answer[:-1]
'''