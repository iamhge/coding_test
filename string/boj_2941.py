# 크로아티아 알파벳
import sys

S = sys.stdin.readline().rstrip()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# 내 코드 (기존)
'''
result = 0

for cAlpha in croatia:
    # print("cAlpha : %s" %cAlpha)
    cIndex = S.find(cAlpha)
    while (cIndex != -1):
        # "_"로 변경하지 않고 비워버리기만 한다면
        # 다른 문자와 합쳐지며 다른 문자로 인식됨.
        # ex) ddz=z= -> 'dz='를 먼저 제외
        #     dz= -> 'd'와 'z='인데 'dz='으로 인식된다.
        S = S.replace(cAlpha, "_", 1)
        result += 1
        # print("S : %s" %S)
        cIndex = S.find(cAlpha)

# "_"로 바꾼 것 다시 변경
S = S.replace("_", "")
result += len(S)

print(result)
'''

# 다른 사람 코드 참고 -> 더 간단
for cAlpha in croatia:
    S = S.replace(cAlpha, "_")

result = len(S)

print(result)