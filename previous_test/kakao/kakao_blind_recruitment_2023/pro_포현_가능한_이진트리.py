# 포화 가능한 이진트리
'''
<해설 조금 본 문제>
- 루트노드가 0이어도 자식 노드들이 모두 더미노드이면 가능하다.
<소감>
- 어디서 풀어본 것 같은데.. 했는데 생각해보니 내가 이 때 코테 봤었네..
- 문제 제대로 보자..!
'''

def decimal2binary(num):
    result = ""
    while num > 0:
        result += str(num%2)
        num //= 2
    return result[::-1]

def isBinaryTree(binary):
    if len(binary) == 1:
        return True
    elif len(binary)%2 == 0:
        return False
    elif binary[len(binary)//2] != "1" and len(set(binary)) != 1:
        return False
    return isBinaryTree(binary[:len(binary)//2]) and isBinaryTree(binary[len(binary)//2+1:])

def makeOnePossible(binary):
    result = 0
    for i in range(0, len(binary), 2):
        if isBinaryTree("0"*i + binary):
            result += 1
    if result == 1:
        return True
    return False

def solution(numbers):
    answer = []
    
    for number in numbers:
        binary = decimal2binary(number)
        if len(binary) % 2 != 1:
            binary = "0" + binary

        if makeOnePossible(binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer