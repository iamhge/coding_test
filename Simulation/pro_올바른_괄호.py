# 올바른 괄호
def solution(s):
    length = len(s)
    temp = 0
    
    for i in range(0, length):
        if s[i] == '(':
            temp += 1
        else:
            temp -= 1
            
        # temp가 0보다 작아진다는 것은 '('가 나오기 전에 ')'가 나왔다는 것을 의미한다.
        if temp < 0:
            return False
        
    # temp가 0이어야 '('과 ')'의 개수가 같다
    if temp != 0:
        return False

    return True