# N개의 최소공배수
'''
<개념>
  유클리드 호제법
<참고 링크>
  유클리드 호제법 - 위키백과 : https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
'''

# 최대공약수를 구한다.
def euclideanAlgorithm(n, m):
    while m % n != 0:
        remainder = m % n
        m = n
        n = remainder
    return n

# 최소공배수를 구한다.
def LCM(n, m):
    GCF = euclideanAlgorithm(n, m)
    return (n // GCF) * (m // GCF) * GCF

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = LCM(answer, arr[i])
    return answer