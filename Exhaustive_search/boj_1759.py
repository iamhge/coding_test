# 암호 만들기
'''
<아이디어>
  1. 조합을 활용하여 해결
  2. 알고보니 파이썬은 combination함수가 이미 따로 있다.. 충격
<개념>
  * 조합 : 서로 다른 n개 중에 r개를 선택하는 경우의 수 (순서 상관 X)
    공식) nCr = n-1Cr-1 + n-1Cr (여기서는 사용하지 않으나, 개수를 구할 때는 사용할 수 있을 듯)
<참고>
  [Algorithm] 순열 조합 알고리즘 개념과 예제 (구현)
   : https://coding-factory.tistory.com/607
  [ 순열과 조합 구현 ] - 재귀를 통한 구현(1 - 조합) (C++)
   : https://yabmoons.tistory.com/99
<틀린 이유>
  * 처음에 자음 2개이상을 생각 안함.
'''
import sys

input = sys.stdin.readline

def checkValid(string):
    vowel = 0
    consonant = 0
    for c in string:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowel += 1
        else:
            consonant += 1
    
    if vowel >= 1 and consonant >= 2:
        return True

    return False

# Select[i] : i번째 알파벳을 뽑았는 지의 여부
# idx : idx 다음부터 r-n개를 뽑는다.
# n : 지금까지 뽑은 개수
# r : 뽑고자하는 개수
def combination(Select, C, A, idx, n, r):
    # r개 만큼 뽑은 경우
    if n == r:
        string = ''
        for i in range(C):
            if Select[i] == True:
                string += A[i]
        if checkValid(string):
            print(string)
        return
    
    # 더 뽑아야 할 경우
    for i in range(idx, C):
        if Select[i] == True:
            continue
        Select[i] = True
        combination(Select, C, A, i, n+1, r) # i번째를 선택했을 경우의 다음 조합
        Select[i] = False # i번째를 선택하지 않은 다음 조합을 찾기 위해 False 처리

def main():
    L, C = map(int, input().split())
    A = list(input().split())
    A.sort()
    Select = [False]*C
    
    combination(Select, C, A, 0, 0, L)

if __name__ == "__main__":
    main()

# 다른 사람 코드
# 파이썬 내장함수를 활용. 오직 valid검사만 해주면 됨.
'''
import itertools

vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
alphabet_list = list(map(str, input().split()))
result = []

for alpha_set in list(itertools.combinations(alphabet_list, L)):
    vowel_cnt, consonant_cnt = 0, 0
    for alpha in sorted(alpha_set):
        if alpha in vowel:
            vowel_cnt += 1
        elif alpha not in vowel:
            consonant_cnt += 1
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        result.append(''.join(sorted(alpha_set)))

for element in sorted(list(set(result))):
    print(element)
'''