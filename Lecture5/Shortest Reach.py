import queue

def BFS(G, dist, visited, s):
    dist[s] = 0
    visited[s] = True
    q = queue.Queue()
    q.put(s)
    while q.empty() == False:
        u = q.get()
        for v in G[u]:
            if visited[v] == False:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.put(v)

q = int(input())
while q > 0:
    n, m = map(int, input().split())
    dist = [-1] * 1005
    visited = [False] * 1005
    G = [[] for i in range(1, 1005)]
    for i in range(m):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    s = int(input())
    BFS(G, dist, visited, s)
    for i in range(1, n + 1):
        if i == s:
            continue
        if dist[i] == -1:
            print(-1, end=' ')
        else: print(dist[i] * 6, end=' ')
    print()
    q -= 1