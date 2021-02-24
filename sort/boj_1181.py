# 단어 정렬
import sys

N = int(sys.stdin.readline().rstrip())
strSet = set()
for _ in range(N):
    strSet.add(sys.stdin.readline().rstrip())

strSet = sorted(strSet) # 알파벳 순 정렬
for string in sorted(strSet, key=lambda str: len(str)): # 길이 순 정렬
    print(string)


# 다른 사람 코드
# len에 따라 bucket에 넣고 나중에 해당 len을 갖는 string들을 sort해서 print
'''
import sys
read = sys.stdin.readline

bucket = [set() for _ in range(53)]

for _2 in range(int(read())):
    word = read()
    bucket[len(word)].add(word)

[print(''.join(sorted(x)), end='') for x in bucket]
'''