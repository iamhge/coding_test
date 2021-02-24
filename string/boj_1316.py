# 그룹 단어 체커
import sys

def isGroupWord(S: str) -> bool:
    count = {}
    for i in range(len(S)):
        try: 
            count[S[i]] += 1
            if S[i] != S[i-1]:
                return False
        except:
            count[S[i]] = 1
    return True

N = int(sys.stdin.readline().rstrip())
result = 0

for i in range(N):
    S = sys.stdin.readline().rstrip() 
    if isGroupWord(S):
        result += 1

print(result)

# 다른 사람 코드 1 (집합 이용)
'''
import sys
N = int(input())

res = 0
for i in range(N):
    s = sys.stdin.readline().rstrip()

    a = 0
    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            a += 1

    if a == len(set(s))-1:
        res += 1

print(res)
'''

# 다른 사람 코드 2 (dict이 아닌, list find 이용)
'''
def group_word(s):
    l = []
    # 단어 한 char씩 순회하며, k가 l에 없었거나,
    # 앞에 해당 char가 l의 직전에 들어가 있으면
    for i in s:
        k = s.find(i)
        if k not in l or k == l[-1]:
            l.append(k)
        else:
            return False
    return True

t = int(input())
sum = 0
for i in range(t):
    if group_word(input()):
        sum +=1
print(sum)
'''