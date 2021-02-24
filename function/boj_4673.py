def d(n: int) -> int:
    strN = str(n)
    result = n
    for elem in strN:
        result += int(elem)
    return result

# 너무 오래걸림
# result = list(range(1,10001))
# for elem in result:
#     elem_temp = elem
#     while(elem_temp <= 10000):
#         elem_temp = d(elem_temp)
#         if elem_temp in result:
#             result.remove(elem_temp)

# 하나라도 self넘버가 있으면 아니므로 한번만 돌리면 됨.
arr = [0] * 10000

for i in range(10000):
    if (d(i) < 10000):
        arr[d(i)] = 1

for i in range(10000):
    if arr[i] == 0:
        print(i)