import queue


INF = int(10e13)
N, M, k, x = map(int, input().split())


class Node:
    def __init__(self, idx, cost):
        self.idx = idx
        self.cost = cost
    def __lt__(self, other):
        return self.cost <= other.cost


def Dijkstra(graph, dist, s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.idx
        w = top.cost
        if dist[u] != w:
            continue
        for v in graph[u]:
            if w + v.cost < dist[v.idx]:
                dist[v.idx] = w + v.cost
                pq.put(Node(v.idx, dist[v.idx]))


def Dijkstra2(graph, s, t):
    dist = [INF] * (N+1)
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    res = INF
    while not pq.empty():
        top = pq.get()
        u = top.idx
        w = top.cost
        if u == t:
            res = w
            return res
        if dist[u] != w:
            continue
        for v in graph[u]:
            if w + v.cost < dist[v.idx]:
                dist[v.idx] = w + v.cost
                pq.put(Node(v.idx, dist[v.idx]))
    return res


graph = [[] for _ in range(N+1)]
chocolate = list(map(int, input().split()))
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))

A, B = map(int, input().split())
dist1 = [INF]*(N+1)
Dijkstra(graph, dist1, A)
min_time = INF
for city in chocolate:
    cost = dist1[city] + Dijkstra2(graph, city, B)
    min_time = min(min_time, cost)
if min_time < x:
    print(min_time)
else:
    print(-1)