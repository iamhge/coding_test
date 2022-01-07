# 카펫

def solution(brown, yellow):
    # h = yellow의 세로 길이
    for h in range(1, yellow+1):
        if yellow % h == 0:
            # w = yellow의 가로 길이
            w = yellow // h
            if (w + 2) * (h + 2) == brown + yellow:
                return [w + 2, h + 2]