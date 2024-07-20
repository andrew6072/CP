class Edge(object):
    def __init__(self, start, target, cost):
        self.start = start
        self.target = target
        self.cost = cost
    def __str__(self):
        return f'{self.start} {self.target} {self.cost}'

INF = 10**9
def BellmanFord(m, n, graph, dist, s):
    dist[s] = 0
    relaxed = True
    for _ in range(n - 1): # n-1 because in worst case algo will traverse through all vertices
        if not relaxed:
            break
        relaxed = False
        for j in range(m):
            u = graph[j].start
            v = graph[j].target
            w = graph[j].cost
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                relaxed = True


graph = []
n = int(input())
for i in range(2, n + 1):
    arr = list(input().split())
    for j, a in enumerate(arr):
        if a != 'x':
            a = int(a)
            edge1 = Edge(i, j + 1, a)
            edge2 = Edge(j + 1, i, a)
            graph.append(edge1)
            graph.append(edge2)

m = len(graph)
dist = [INF for _ in range(n+1)]
BellmanFord(m, n, graph, dist, 1)
print(max(dist[1:]))