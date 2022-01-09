# 타겟 넘버
'''
<풀이 방법>
  ex)
  3 3 2 1 -> 3

  numbers를 모두 더하면 9
  target까지 -3을 만들어야 한다. (9 - 6 = 3이고, 6 // 2 = 3 이므로)
  따라서 numbers를 순회하면서,
  해당 index의 num이 minus보다 작으면 (index-1, minus-num)를 stack에 넣는다. (해당 index의 num을 빼는 경우)
  해당 index의 num이 minus와 같으면 result += 1한다.
  그리고 무조건 (index-1, minus)를 넣는다. (해당 index의 num을 더하는 경우)

  3 + 3 - 2 - 1 = 3 
  3 - 3 + 2 + 1 = 3
  - 3 + 3 + 2 + 1 = 3
'''
from collections import deque

def DFS(numbers, root):
    stack = deque([root])
    result = 0
    
    while stack:
        i, minus = stack.popleft()
        
        if i < 0: # 모든 numbers를 순회한 경우
            continue
        if numbers[i] < minus:
            stack.append((i-1, minus-numbers[i])) # numbers[i]를 빼는 경우
        elif numbers[i] == minus: # target이 만들어진 경우
            result += 1
        stack.append((i-1, minus)) # numbers[i]를 더하는 경우
        
    return result

def solution(numbers, target):
    if sum(numbers) == target:
         return 1
    minus = (sum(numbers) - target) // 2
    return  DFS(numbers, (len(numbers)-1, minus))

# 다른 사람 풀이
'''
<풀이 방법>
  - 내 방식 처럼 굳이 minus 개념을 도입하지 않고 target자체로 비교하면 된다.(이거 보고나니 나 왜 굳이 minus 기준으로 계산했던거지 싶다.)
  - 마찬가지로 더하는 경우, 빼는 경우를 넣는다.
  - 재귀함수를 이용해 DFS를 구현했다.
'''
'''
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''