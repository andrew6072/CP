# test cases:50
# V:100 E:5000
# Time complexity: 50*100*(100+5000)
import queue

def BFS(graph, dist, s):
    visited = [False]*101
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.put(v)


def BFS2(graph, s, t):
    visited = [False] * 101
    dist = [-1] * 101
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
    visited[s] = True
    res = -1
    while not q.empty():
        u = q.get()
        if u == t:
            res = dist[u]
            return res
        for v in graph[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.put(v)
    return res



# remain 2 lists, first one stores distance from s to an arbitrary vertex,
# second one stores distance from an arbitrary vertex
tc = int(input())
for i in range(tc):
    dist1 = [-1]*101

    graph = [[] for _ in range(101)]
    N = int(input())
    R = int(input())
    for _ in range(R):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s, t = map(int, input().split())

    max_time = -1
    BFS(graph, dist1, s)
    for u in range(101):
        cost = dist1[u] + BFS2(graph, u, t)
        max_time = max(max_time, cost)
    print(f'Case {i+1}: {max_time}')
