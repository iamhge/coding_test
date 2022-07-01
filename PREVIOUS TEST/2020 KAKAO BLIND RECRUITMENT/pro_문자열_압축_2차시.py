# 문자열 압축 2차시
'''
<교훈>
  - 문제를 똑바로 읽자.. 문제 제대로 안읽어서 이상하게 풀고 있었음 ㅠ.ㅠ
'''
def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1
    
    for unit in range(1, len(s)):
        compress = ''
        repeat = 1
        now = unit
        while now + unit <= len(s):
            # print("now : ", now)
            # print("repeat : ", repeat)
            # print("now 앞 : ", s[now-unit:now])
            # print("now 뒤 : ", s[now:now+unit])
            # print("compress : ", compress)
            if s[now-unit:now] != s[now:now+unit]:
                if repeat > 1:
                    compress += str(repeat)
                compress += s[now-unit:now]
                repeat = 1
            else:
                repeat += 1
            now += unit
            # print("변환 뒤")
            # print("compress : ", compress)
            # print()
        
        if repeat > 1:
            compress += str(repeat)
        compress += s[now-unit:now]
            
        # print("result : ", compress + s[now:])
        # print("************************")
        answer = min(answer, len(compress + s[now:]))
            
    return answer