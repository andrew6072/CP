import queue


class Node:
    def __init__(self, idx, cost):
        self.idx = idx
        self.cost = cost
    def __lt__(self, other):
        return self.cost <= other.cost


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


INF = int(10e9)
MAX = int(10e4)

tc = int(input())
for _ in range(tc):
    graph = [[] for _ in range(MAX + 5)]
    ans = []
    n, m, k, s, t = map(int, input().split())
    for _ in range(m):
        d, c, l = map(int, input().split())
        graph[d].append(Node(c, l))
    for _ in range(k):
        u, v, q = map(int, input().split())
        u_or_v_is_popped = -2
        old_node = None

        for i, o in enumerate(graph[u]):
            if o.idx == v:
                u_or_v_is_popped = 1
                old_node = graph[u][i]
                del graph[u][i]
                break
        if old_node != None:
            for i, o in enumerate(graph[v]):
                if o.idx == u:
                    u_or_v_is_popped = -1
                    old_node = graph[v][i]
                    del graph[v][i]
                    break

        # Update graph base on the proposed two-way route
        graph[u].append(Node(v, q))
        graph[v].append(Node(u, q))

        # Use Dijkstra to find best route from "s" to "t"
        dist = [INF]*(MAX + 5)
        Dijkstra(dist, s) # O(mlog(n))
        min_cost = dist[t]
        if min_cost != INF:
            ans.append(dist[t])

        # Recover the old graph
        graph[u].pop()
        graph[v].pop()
        if u_or_v_is_popped == 1:
            graph[u].append(old_node)
        elif u_or_v_is_popped == -1:
            graph[v].append(old_node)
    # Find min route from array ans
    if len(ans) == 0:
        print(-1)
    else:
        res = INF
        for x in ans:
            if x < res:
                res = x
        print(res)