import queue


class Node:
    def __init__(self, idx, cost):
        self.idx = idx
        self.cost = cost
    def __lt__(self, other):
        return self.cost <= other.cost

def Dijkstra(graph, dist, path, s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.idx
        w = top.cost
        for neighbor in graph[u]:
            v = neighbor.idx
            q = neighbor.cost
            if w + q < dist[v]:
                dist[v] = w + q
                pq.put(Node(v, dist[v]))
                path[v] = u


# helper function deletes connection between u and v
def helper(graph, u, v):
    for i, o in enumerate(graph[u]):
        if o.idx == v:
            del graph[u][i]
            break


def deleteShortest(graph, path, s, t):
    i = t
    while i != s and i != -1:
        helper(graph, path[i], i)
        i = path[i]

N, M = -1, -1
while N != 0 and M != 0:
    N, M = map(int, input().split())
    if N != 0 and M != 0:
        S, D = map(int, input().split())
        INF = int(10e9)
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            u, v, w = map(int, input().split())
            graph[u].append(Node(v, w))
        path = [-1]*(N+1)
        dist = [INF]*(N+1)
        Dijkstra(graph, dist, path, S)
        shortest_len = dist[D]
        deleteShortest(graph, path, S, D)

        # this code is to handle multiple shortest paths with same length in graph
        test_len = shortest_len
        while test_len == shortest_len:
            path1 = [-1] * (N + 1)
            dist1 = [INF] * (N + 1)
            Dijkstra(graph, dist1, path1, S)
            test_len = dist1[D]
            if test_len == shortest_len:
                deleteShortest(graph, path1, S, D)

        path2 = [-1]*(N+1)
        dist2 = [INF]*(N+1)
        Dijkstra(graph, dist2, path2, S)
        ans = dist2[D]
        if ans == INF:
            print(-1)
        else:
            print(ans)