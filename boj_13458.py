# 시험 감독
import sys
input = sys.stdin.readline

def solution(N, A, B, C):
    answer = 0
    
    for a in A:
        a -= B
        answer += 1
        if a > 0:
            answer += (a // C) + (1 if a % C > 0 else 0)
    return answer

def main():
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    print(solution(N, A, B, C))

main()