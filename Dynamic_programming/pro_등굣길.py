# 등굣길
def solution(m, n, puddles):
    routes = [[0 for _ in range(m+1)] for _ in range(n+1)]
    routes[1][1] = 1
    
    for x in range(1, m+1):
        for y in range(1, n+1):
            if [x, y] not in puddles:
                routes[y][x] += (routes[y][x-1] + routes[y-1][x]) % 1000000007

    return routes[n][m]

# 시간 초과
'''
def solution(m, n, puddles):
    routes = [[0 for _ in range(m+1)] for _ in range(n+1)]
    routes[1][1] = 1
    
    def mySolution(x, y, m, n, puddles):
        routes[y][x] %= 1000000007
        if [x, y] not in puddles:
            if x < m:
                routes[y][x+1] += 1
                mySolution(x+1, y, m, n, puddles)
            if y < n:
                routes[y+1][x] += 1
                mySolution(x, y+1, m, n, puddles)
        
    mySolution(1, 1, m, n, puddles)
    return routes[n][m]
'''