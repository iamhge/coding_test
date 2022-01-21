# 2개 이하로 다른 비트
'''
<풀이 방법>
  1) num을 이진수 binNum으로 변환한다.
  2) binNum의 가장 작은 비트부터 검사하여, binNum[i] == '0'이 최초로 나오는 i에서
    2-1) i == len(binNum)-1 (즉 이진수에서 1을 나타내는 자릿수) 이면 해당 비트만 1로 바꾼다.
         -> 1개를 바꾸어 가장 작은 수를 만듦.
    2-2) i < len(binNum)-1 라면
        2-2-1) binNum[i+1] == '1'이므로, binNum[i]를 '0'으로, binNum[i+1]을 '1'로 바꾼다. 
               -> 2개를 바꾸어 가장 작은 수를 만듦.
  3) binNum을 모두 검사했는데, '0'이 나오지 않는다면
    3-1) 가장 큰 비트를 '0'으로 그 위 비트를 '1'로 변경한다.
         -> 2개를 바꾸어가장 작은 수를 만듦.
<반례>
  ex) input
      [1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]
      output
      [1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101]
'''
def myDecimal(binNum):
    result = 0
    binNum = binNum[::-1]
    for i in range(0, len(binNum)):
        result += 2**i * int(binNum[i])
    return result

def solution(numbers):
    answer = []
    for num in numbers:
        binNum = str(bin(num))[2:]
        for i in range(len(binNum)-1, -1, -1):
            if binNum[i] == '0':
                binNum = binNum[:i] + '1' + binNum[i+1:]
                if i != len(binNum)-1:
                    binNum = binNum[:i] + '10' + binNum[i+2:]
                break
        else:
            binNum = '10' + binNum[1:]
        answer.append(myDecimal(binNum))
    return answer