# 이분 그래프
import sys
from collections import deque

input = sys.stdin.readline

def DFS(vertex: dict, root: int, visited: list):    
    stack = deque([root])
    visited[root] = True

    while stack:
        n = stack.pop()

        for f in vertex[n]:
            if visited[f] == -1:
                stack.append(f)
                visited[f] = not visited[n]
            if visited[f] == visited[n]:
                return False, visited

    return True, visited


def main():
    K = int(input().rstrip())
    for __ in range(K):
        V, E = map(int, input().split())
        vertex = {i: set() for i in range(1, V+1)}

        for _ in range(E):
            a, b = map(int, input().split())
            vertex[a].add(b)
            vertex[b].add(a)

        # 미방문 : -1, 방문 : True or False 
        visited = [-1]*(V+1)
        result = "YES"
        for i in range(1, V+1):
            if visited[i] == -1:
                res, visited = DFS(vertex, i, visited)
                if res == False:
                    result = "NO"
                    break
        
        print(result)

if __name__=="__main__":
    main()