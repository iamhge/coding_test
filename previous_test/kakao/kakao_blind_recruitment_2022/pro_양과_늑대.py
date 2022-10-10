# 양과 늑대
def dfs(now, sheep, wolf, info, graph, visited, cango):
    if info[now] == 0: # 양
        sheep += 1
    else: # 늑대
        wolf += 1
    result = sheep
    '''
    # test
    print("now: ", now)
    print("sheep: ", sheep)
    print("wolf: ", wolf)
    print("visited: ", visited)
    print("cango: ", cango)
    print()
    '''
    
    if sheep <= wolf:
        return 0

    for idx, nextNode in enumerate(cango):
        if nextNode not in visited:
            tmp = cango.copy()
            tmp.extend(graph[nextNode])
            tmp.pop(idx)
            visited.append(nextNode)
            result = max(result, dfs(nextNode, sheep, wolf, info, graph, visited.copy(), tmp))
            visited.pop()
    return result

def solution(info, edges):
    graph = {i: [] for i in range(len(info))}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    return dfs(0, 0, 0, info, graph, [0], graph[0])