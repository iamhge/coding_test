import sys

T = int(sys.stdin.readline().rstrip())

# dist   : 1 2 3 4 5 6 7 8 9 ...
# result : 1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 ...
# 연속되는 result 반복 횟수 : 1번 1번 2번 2번 3번 3번 4번 4번... (i번이 2회씩 반복)
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    dist = (y - x)

    # 최소 횟수가 반복되는 수
    # dist = 7일 때, result는 5이고
    # 전체에서 5는 3번(= i) 연속된다.
    i = 0
    while dist > 0:
        i += 1
        dist -= 2 * i
        
    dist += 2 * i

    if dist <= i: # 앞 파트
        result = 2 * i - 1
    else: # 뒷 파트
        result = 2 * i

    print(result)

# 다른 사람 코드 너무 다양함 궁금하면 인터넷쳐보삼
# https://m.blog.naver.com/PostView.nhn?blogId=occidere&logNo=220982644540&proxyReferer=https:%2F%2Fwww.google.com%2F -> 내 생각의 깔끔한버전!!!!!!
# https://ooyoung.tistory.com/91 -> 나랑 비슷 count : result, move : i
# https://pacific-ocean.tistory.com/124 -> 제곱근
# https://zifmfmphantom.tistory.com/14 