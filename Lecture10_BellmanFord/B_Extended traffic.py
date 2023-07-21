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
            return
        relaxed = False
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                relaxed = True
    for _ in range(n-1):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = -INF

INF = 10**14
tc = int(input())
for i in range(tc):
    input()
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    graph = []
    dist = [INF for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph.append(Edge(u, v, (a[v-1] - a[u-1])**3))
    BellmanFord(n, m, dist, graph, 1)
    Q = int(input())
    print(f'Case {i+1}:')
    for _ in range(Q):
        q = int(input())
        ans = dist[q]
        if ans < 3 or abs(ans) == INF:
            print('?')
        else:
            print(ans)
