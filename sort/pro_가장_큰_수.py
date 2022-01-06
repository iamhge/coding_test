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