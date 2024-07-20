import sys
sys.setrecursionlimit(10005)

def dfs(u, ans, visited, flag, graph):
    visited[u] = True
    flag[u] = True
    for v in graph[u]:
        if flag[v]:
            ans = 'YES'
            return
        if visited[v]:
            continue
        else:
            dfs(u, ans, visited, flag, graph)

def Solve(n, graph):
    ans = False
    flag = [False] * (10**4 + 5)
    visited = [False] * (10**4 + 5)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, ans, visited, flag, graph)
    return


t = int(input())
while t > 0:
    G = [[] for _ in range(10**4 + 5)]
    N, M = map(int, input().split())

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
    Solve(N, G)
    t -= 1