import queue

X, L = map(int, input().split())
N = int(input())
Y = list(map(int, input().split()))
M = 100000

def BFS(X, L):
    q = queue.Queue()
    q.put(X)
    dist = [-1] * (M+5)
    dist[X] = 0
    while not q.empty():
        u = q.get()
        for y in Y:
            v = (u * y) % M
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if v == L:
                    return dist[v]
                q.put(v)
    return -1


print(BFS(X, L))