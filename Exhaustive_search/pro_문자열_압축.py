# 문자열 압축
def solution(s):
    answer = len(s)
    
    for unit in range(1, len(s)//2+1):
        i = 0
        zippedS = ''
        while i < len(s):
            now = 1
            while s[i:i+unit] == s[i+unit:i+2*unit]:
                now += 1
                i += unit
            if now != 1:
                zippedS += str(now) + s[i:i+unit]
            else:
                zippedS += s[i:i+unit]
            i += unit
        answer = min(answer, len(zippedS))
    
    return answer

# 다른 사람 코드
'''
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
'''