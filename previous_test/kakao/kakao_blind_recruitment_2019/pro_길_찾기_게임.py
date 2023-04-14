# 길 찾기 게임
'''
<풀이 방법>
left = x좌표 왼쪽에 있는 노드 중, 나보다 작으면서 가장 큰 y 값
right = x좌표 오른쪽에 있는 노드 중, 나보다 작으면서 가장 큰 y 값
<소감>
- preorder, postorder 구현은 어렵지 않다.
- 그런데 tree로 만드는 과정이 정!말! 어려웠다.
- 2시간 걸렸다 ㅠㅠㅠ 분발하자...
'''
import sys
sys.setrecursionlimit(100000)

from collections import defaultdict

def preorder(node, vertex):
    # leafnode
    if node == 0:
        return []
    
    result = []
    
    result.append(node)
    result.extend(preorder(vertex[node][0], vertex))
    result.extend(preorder(vertex[node][1], vertex))

    return result

def postorder(node, vertex):
    # leafnode
    if node == 0:
        return []
    
    result = []
    
    result.extend(postorder(vertex[node][0], vertex))
    result.extend(postorder(vertex[node][1], vertex))
    result.append(node)
    
    return result

# nodes: x기준 sort되어 있는 상태의 노드명
def makeTree(nodes, vertex, nodedict):
    if len(nodes) <= 0:
        return 0
    
    root = max(nodes, key=lambda x: nodedict[x][1])
    
    rootidx = nodes.index(root)
    leftnodes = nodes[:rootidx]
    rightnodes = nodes[rootidx+1:]
    
    # left subtree
    left = makeTree(leftnodes, vertex, nodedict)
    # right subtree
    right = makeTree(rightnodes, vertex, nodedict)

    vertex[root] = [left, right]
    
    return root
        
def solution(nodeinfo):
    answer = [[]]
    nodedict = {(i+1): nodeinfo[i] for i in range(len(nodeinfo))}
    
    # vertex[node] = [left, right]
    vertex = {}
    
    # x기준으로 정렬한 노드명
    nodes = sorted(nodedict, key=lambda x: nodedict[x])
    
    root = makeTree(nodes, vertex, nodedict)

    return [preorder(root, vertex), postorder(root, vertex)]