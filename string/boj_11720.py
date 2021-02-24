import sys

N = int(sys.stdin.readline().rstrip())

# 1) list로 만들어서 ['1', '2', '3'] 형태로 만듦.
# 2) map으로 int형으로 변환 1, 2, 3
# 3) 2)의 결과를 list로 변환 -> [1, 2, 3]
num = list(map(int, list( sys.stdin.readline().rstrip() )))
print(sum(num))