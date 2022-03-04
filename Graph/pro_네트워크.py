# 네트워크
from collections import deque

def dfs(root, n, computers, visited):
    stack = deque([root])
    
    while stack:
        now = stack.pop()
        visited[now] = True
        
        for i in range(n):
            if (computers[now][i] == 1) and (not visited[i]):
                stack.append(i)
    
    return visited

def solution(n, computers):
    networks = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            visited = dfs(i, n, computers, visited)
            networks += 1
    
    return networks