import sys

string = list(sys.stdin.readline().rstrip())
result = [-1] * 26

for char in string:
    result[ord(char) - 97] = string.index(char)

for elem in result:
    print(elem, end=' ')

# 다른 사람 코드 (모든 알파벳 하나씩 찾기)
'''
string=input()
print(*[string.find(chr(i+97)) for i in range(26)])
'''