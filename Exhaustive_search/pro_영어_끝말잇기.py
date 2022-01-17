# 영어 끝말잇기
def solution(n, words):
    already = [words[0]]
    
    for i in range(1, len(words)):
        if (words[i] in already) or words[i][0] != words[i-1][-1]:
            return [i%n+1, i//n+1]
        already.append(words[i])

    return [0, 0]