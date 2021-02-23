# 잃어버린 괄호
'''
<아이디어>
  + 앞뒤로는 모두 더해주고 다 빼주면 됨
<참고>
  아이디어는 있는데 어케 구현할지 멀겠어서 다른 사람 코드 참고함 ㅜㅜ
  [백준] 1541번(python 파이썬)
   : https://pacific-ocean.tistory.com/228
'''
import sys

exp = sys.stdin.readline().rstrip()
splitNums = exp.split('-')
minus = [0]*len(splitNums)

for i in range(len(splitNums)):
    tmp = splitNums[i].split('+')
    for j in tmp:
        minus[i] += int(j)

result = minus[0]
for i in range(1, len(minus)):
    result -= minus[i]

print(result)