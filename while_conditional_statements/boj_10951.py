# A+B - 4
import sys
while 1:
    try: # 실행할 코드
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except: # 예외가 발생했을 때 처리하는 코드
        break