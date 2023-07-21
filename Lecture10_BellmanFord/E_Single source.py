class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BellmanFord(n, m, dist, graph, s):
    dist[s] = 0
    relaxed = True
    for _ in range(n-1):
        if relaxed == False:
            break
        relaxed = False
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                relaxed = True
    found = True
    for _ in range(n-1):
        if found == False:
            break
        found = False
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = -INF
                found = True

INF = 10**9
n, m, q, s = -1, -1, -1, -1
while n != 0 or m != 0 or q != 0 or s != 0:
    n, m, q, s = map(int, input().split())
    if n != 0 or m != 0 or q != 0 or s != 0:
        graph = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph.append(Edge(u, v, w))
        dist = [INF for _ in range(n)]
        BellmanFord(n, m, dist, graph, s) # O(E*V)
        for _ in range(q):
            t = int(input())
            ans = dist[t]
            if ans == INF:
                print('Impossible')
            elif ans == -INF:
                print('-Infinity')
            else:
                print(ans)
        print()