# 가장 큰 수
'''
알고리즘을 모르겠어서 다른 사람 코드 참고함.
반례 찾기가 너무 힘듦. 질문하기에서 참고함.
<반례>
  ex1) [0, 0, 0] -> "0"
  ex2) [1, 10, 100, 1000] -> "1101001000"
  ex3) [1231, 123] -> "1231231"
<참고>
  프로그래머스 질문하기
   : https://programmers.co.kr/questions/24627
  파이썬 정렬, 다중 조건으로 한 번에 하기.
   : https://dailyheumsi.tistory.com/67
'''
# num을 4자리까지 반복한다 ex) 1 -> 1111, 12 -> 1212, 10 -> 1010
def extendNum(num):
    return str(num*4)[:4]

def solution(numbers):
    answer = ""
    myNums = [(extendNum(str(num)), num) for num in numbers]
    myNums.sort(key = lambda x: (x[0], -x[1]), reverse = True)
    
    for num in myNums:
        answer += str(num[1])
    
    if answer[0] == "0":
        answer = "0"
    
    return answer

# 다른 사람 풀이
'''
앞 뒤로 더해서 비교하는 함수를 추가.
이걸 어떻게 떠올려 ㅠ.ㅠ
'''
'''
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
'''