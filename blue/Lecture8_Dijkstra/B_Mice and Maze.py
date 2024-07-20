import queue


class Node:
    def __init__(self, idx, cost):
        self.idx = idx
        self.cost = cost
    def __lt__(self, other):
        return self.cost <= other.cost

N = int(input())
E = int(input())
T = int(input())
M = int(input())
graph = [[] for _ in range(105)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))


INF = int(10e9)

def Dijkstra(dist, s):
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

count = 1
for i in range(1, N+1):
    if i != E:
        dist = [INF] * 105
        Dijkstra(dist, i)
        if dist[E] <= T:
            count += 1

print(count)