import sys

S = sys.stdin.readline().rstrip()
S = S.upper()

alphaCount = {}
for c in S:
    try: alphaCount[c] += 1
    except: alphaCount[c] = 1 # 기존에 없었다면 새로 생성

# alphaCount[x] : key x의 value
# value가 가장 큰 key값
maxAlpha = max(alphaCount, key = (lambda x: alphaCount[x]))
maxValue = alphaCount[maxAlpha]

for key, value in alphaCount.items():
    if key == maxAlpha:
        continue
    elif value == maxValue:
        maxAlpha = '?'
        break

print(maxAlpha)