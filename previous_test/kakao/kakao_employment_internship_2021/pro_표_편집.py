# 표 편집
'''
<풀이 방법>
- linked list
<오답 노트>
- 시간 복잡도가 관건이었던 문제.
- 명령어 'Z' 입력시, 최근에 삭제되었던 것 순서대로 다시 복구되므로 굳이 재연결할 노드를 탐색하지 않고,
  이전에 table[z]가 연결했던 노드를 그대로 연결하면 된다.
'''
from collections import deque

status = []
table = []

def up(k, x):
    for _ in range(x):
        k = table[k][0]
    return k

def down(n, k, x):
    for _ in range(x):
        k = table[k][1]
    return k

def delete(n, k):
    status[k] = 'X'
    
    # 이전 행과 다음 행 연결
    pre = table[k][0]
    nex = table[k][1]
    
    if pre != -1:
        table[pre][1] = nex
    if nex != -1:
        table[nex][0] = pre
        return nex
    
    return pre

def back(n, z):
    status[z] = 'O'
    
    # 재연결
    # 가장 최근에 삭제된 것 순서대로 복구되므로, table[z]에 저장되어있던 것들로 연결시켜주면된다.
    pre = table[z][0]
    nex = table[z][1]
    if pre != -1:
        table[pre][1] = z
    if nex != -1:
        table[nex][0] = z
    
def solution(n, k, cmd):
    global status, table
    z = deque([])
    status = ['O']*n
    
    # table[i] = [이전 행, 다음 행]
    table = [[-1, 1]]
    for i in range(1, n-1):
        table.append([i-1, i+1]) 
    table.append([n-2, -1])
    
    for c in cmd:
        if c[0] == 'U':
            k = up(k, int(c[2:]))
        elif c[0] == 'D':
            k = down(n, k, int(c[2:]))
        elif c == 'C':
            z.append(k)
            k = delete(n, k)
        else:
            back(n, z.pop())
        # print(k, ''.join(status))
        # print(table)
    
    return ''.join(status)

# 딱 하나 효율성 통과 못함... 시간초과
'''
from collections import deque

status = []
table = []

def up(k, x):
    for _ in range(x):
        k = table[k][0]
    return k

def down(n, k, x):
    for _ in range(x):
        k = table[k][1]
    return k

def delete(n, k):
    status[k] = 'X'
    
    # 이전 행과 다음 행 연결
    pre = table[k][0]
    nex = table[k][1]
    
    if pre != -1:
        table[pre][1] = nex
    if nex != -1:
        table[nex][0] = pre
        return nex
    
    return pre

def back(n, z):
    status[z] = 'O'
    
    # 재연결
    pre = table[z][0]
    nex = table[z][1]
    
    for pre in range(z-1, -1, -1):
        if status[pre] == 'O':
            table[pre][1] = z
            table[z][0] = pre
            break
            
    for nex in range(z+1, n):
        if status[nex] == 'O':
            table[z][1] = nex
            table[nex][0] = z
            break

def solution(n, k, cmd):
    global status, table
    z = deque([])
    status = ['O']*n
    
    # table[i] = [이전 행, 다음 행]
    table = [[-1, 1]]
    for i in range(1, n-1):
        table.append([i-1, i+1]) 
    table.append([n-2, -1])
    
    for c in cmd:
        if c[0] == 'U':
            k = up(k, int(c[2:]))
        elif c[0] == 'D':
            k = down(n, k, int(c[2:]))
        elif c == 'C':
            z.append(k)
            k = delete(n, k)
        else:
            back(n, z.pop())
        print(k, ''.join(status))
        print(table)
    
    return ''.join(status)
'''

# 더 시간 초과
'''
from collections import deque

status = ""
# n = 7, k = 3, x = 1
# 0 1 2 3 4 5 6
# O O X O O O O
# status[::-1] = O O O O X O O
# 
def up(n, k, x): 
    while x > 0:
        k = n-1 - status[::-1].find('O', n-k)
        x -= 1
        
    return k

def down(n, k, x):
    while x > 0:
        k = status.find('O', k+1)
        x -= 1
    return k

def delete(n, k):
    global status
    status = status[:k] + 'X' + status[k+1:]
    
    if k+1 < n:
        downK = status.find('O', k+1)
        if downK != -1:
            return downK
    
    return up(n, k, 1)

def back(z):
    global status
    status = status[:z] + 'O' + status[z+1:]

def solution(n, k, cmd):
    global status
    status = 'O'*n
    z = deque([])
    
    for c in cmd:
        if c[0] == 'U':
            k = up(n, k, int(c[2:]))
        elif c[0] == 'D':
            k = down(n, k, int(c[2:]))
        elif c == 'C':
            z.append(k)
            k = delete(n, k)
        else:
            back(z.pop())
        # print(k, ''.join(status))
    
    return ''.join(status)
'''

# 시간 초과
'''
from collections import deque

status = []

def up(k, x):
    while x > 0:
        while status[k-1] == 'X':
            k -= 1
        x -= 1
        k -= 1
        
    return k

def down(n, k, x):
    while x > 0:
        while status[k+1] == 'X':
            k += 1
        x -= 1
        k += 1
        
    return k

def downForDel(n, k, x):
    while x > 0:
        if k+1 >= n: return -1
        while status[k+1] == 'X':
            k += 1
            if k+1 >= n: return -1  # 문제에서 주어지는 cmd로 일어날 일은 없음.
        x -= 1
        k += 1
    return k

def delete(n, k):
    status[k] = 'X'
    
    downK = downForDel(n, k, 1)
    if downK != -1:
        return downK
    
    return up(k, 1)

def back(z):
    status[z] = 'O'

def solution(n, k, cmd):
    global status
    z = deque([])
    status = ['O']*n
    
    for c in cmd:
        if c[0] == 'U':
            k = up(k, int(c[2:]))
        elif c[0] == 'D':
            k = down(n, k, int(c[2:]))
        elif c == 'C':
            z.append(k)
            k = delete(n, k)
        else:
            back(z.pop())
        # print(k, ''.join(status))
    
    return ''.join(status)
'''