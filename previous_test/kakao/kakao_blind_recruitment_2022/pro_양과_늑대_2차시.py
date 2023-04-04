# 양과 늑대 2차시
'''
<풀이 방법
  1) if 양 <= 늑대: 종료
  2) 이웃 노드 탐색
     탐색 완료한 부모 노드의 자식끼리 재 연결
'''
from collections import defaultdict
import copy

def dfs(now, sheep, wolf, myNode, visited, info):
    if sheep <= wolf:
        return 0
    
    result = sheep
    
    for child in myNode[now]:
        if visited[child]:
            continue
        
        tmpMyNode = copy.deepcopy(myNode)
        
        if info[child] == 0: # 양
            visited[child] = True
            tmpMyNode[child].extend(tmpMyNode[now])
            result = max(result, dfs(child, sheep+1, wolf, tmpMyNode, visited, info))
            visited[child] = False
        else:
            visited[child] = True
            tmpMyNode[child].extend(myNode[now])
            result = max(result, dfs(child, sheep, wolf+1, tmpMyNode, visited, info))
            visited[child] = False

    return result
    
def solution(info, edges):
    answer = 0
    node = defaultdict(list)
    
    visited = [False] * len(info)
    
    for edge in edges:
        node[edge[0]].append(edge[1])
    
    visited[0] = True
    
    return dfs(0, 1, 0, node, visited, info)