'''
<풀이 방법>
  - 등비수열의 합
 
* i번째 글자까지의 순서 = i-1번째 글자까지의 순서 + 5-i개의 글자로 만들 수 있는 단어의 수 + 1
* word의 글자가 차례로 alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabel[m] 일 경우

0 번째 글자(alphabet[i])의 순서
= i * (1 + 5 + 5*5 + 5*5*5 +  5*5*5*5) + 1

1 번째 글자(alphabet[j])까지의 순서
= 0 번째 글자까지의 순서 + j * (1 + 5 + 5*5 + 5*5*5) + 1

2 번째 글자(alphabet[k])까지의 순서
= 1 번째 글자까지의 순서 + k * (1 + 5 + 5*5) + 1

3 번째 글자(alphabet[l])까지의 순서
= 2 번째 글자까지의 순서 + l * (1 + 5) + 1

4 번째 글자(alphabet[m])까지의 순서
= 3 번째 글자까지의 순서 + m * 1 + 1
'''
def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    n = len(word)
    tmp = [5**i for i in range(1, 5)]
    
    for i in range(n):
        for j in range(5):
            if word[i] == alphabet[j]:
                answer += j * (1 + sum(tmp[:4-i])) + 1
                break
    
    return answer

# 다른 사람 코드
'''
<풀이 방법>
  - 길이가 길지 않으므로 모든 경우의 수를 구한 후 리턴한다.
'''
'''
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
'''