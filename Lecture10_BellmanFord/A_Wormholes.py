INF = 10**9
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BellmanFord(dist, graph, s):
    dist[s] = 0
    for _ in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
    for j in range(m):
        u = graph[j].source
        v = graph[j].target
        w = graph[j].weight
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return False
    return True

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    graph = []
    dist = [INF for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u, v, w))
    ans = BellmanFord(dist, graph, 0)
    if not ans:
        print('possible')
    else:
        print('not possible')
