import queue

N = int(input())

G = [[] for _ in range(1000+3)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

Q = int(input())
girls = [0]*1003
for _ in range(Q):
    q = int(input())
    girls[q] = 1

def BFS(girls, G):
    dist_id = [] #pair of distance and id of country of a girl
    visited = [False]*1003
    dist = [-1]*1003
    q = queue.Queue()
    q.put(1)
    dist[1] = 0
    visited[1] = True
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u]+1
                if girls[v] == 1:
                    dist_id.append((dist[v], v))
                q.put(v)
    return dist_id

dist_id = BFS(girls, G)
dist_id.sort(key=lambda s:(s[0], s[1]))
print(dist_id[0][1])