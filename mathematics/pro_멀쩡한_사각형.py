# 멀쩡한 사각형
'''
<풀이 방법>
  - 패턴 * 최대 공약수가 사용할 수 없는 사각형의 개수이다.
  - 패턴의 가로 길이 = w//gcd, 세로 길이 = h//gcd 이다.
  - 패턴에서 대각선이 지나는 칸은 세로 한 줄에서 1칸 ~ 2칸이다
    - 대각선이 지나는 칸은 한줄에서 최소 1칸이다 -> h/gcd 
    - 대각선이 지나는 칸이 2칸일 경우의 수를 이에 더해주면 답.
      - 대각선이 지나는 칸이 2칸일 경우 = w/gcd-1 
<참고>
  [Summer/Winter Coding(2019)] 멀쩡한 사각형 C++
  : https://movingmountain.tistory.com/183?category=951316
'''
def euclidian(a, b):
    remain = a % b
    while remain != 0:
        a = b
        b = remain
        remain = a % b
    return b

def solution(w,h):
    gcd = euclidian(w, h)
    return w*h - (w//gcd + (h//gcd-1))*gcd

# 틀린 코드
'''
기울기를 이용한 풀이법.
개념은 맞지만 내림, 버림 연산 시 부동소수점 문제로 잘못 버리거나 올려서 문제 발생.
'''
'''
import math

def solution(w,h):
    no = 0
    x = euclidian(w, h)
    
    for i in range(1, h//x+1):
        no += math.ceil(w/h*i) - math.floor(w/h*(i-1))
        
    return w*h - no*x
'''