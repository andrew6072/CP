def dfs(visited, graph, s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            dfs(visited, graph, v)


def FindNumComponents(n, graph):
    visited = [False]*(10**5+3)
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(visited, graph, i)
            count += 1
    return count


t = int(input())

for _ in range(t):
    N = int(input())
    e = int(input())
    G = [[] for _ in range(10 ** 5 + 3)]
    for _ in range(e):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    count = FindNumComponents(N, G)
    print(count)
