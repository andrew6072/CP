import queue


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
        for v in graph[u]:
            if w + v.cost < dist[v.idx]:
                dist[v.idx] = w + v.cost
                pq.put(Node(v.idx, dist[v.idx]))


INF = int(10e9)
tc = int(input())
for i in range(tc):
    n, m, s, t = map(int, input().split())
    graph = [[] for _ in range(20005)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    dist = [INF]*(20005)
    Dijkstra(graph, dist, s)
    ans = dist[t]
    if ans != INF:
        print(f'Case #{i+1}: {ans}')
    else:
        print(f'Case #{i+1}: unreachable')