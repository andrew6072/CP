import queue


class Node:
    def __init__(self, index, dist):
        self.dist = dist
        self.index = index
    def __lt__(self, other):
        return self.dist <= other.dist
    def __str__(self):
        return f'index = {self.index}\ndist = {self.dist}'

G = [[] for _ in range(501)]
INF = 10e9
N = int(input())
for _ in range(N):
    u, v, w = map(int, input().split())
    G[u].append(Node(v, w))
    G[v].append(Node(u, w))


distance = [INF]*501
path = [-1]*501
def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    distance[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.index
        w = top.dist
        for neighbor in G[u]:
            if w + neighbor.dist < distance[neighbor.index]:
                distance[neighbor.index] = w + neighbor.dist
                pq.put(Node(neighbor.index, distance[neighbor.index]))
                path[neighbor.index] = u

start = int(input())
Dijkstra(start)
Q = int(input())
for _ in range(Q):
    end = int(input())
    ans = distance[end]
    if ans == INF:
        print('NO PATH')
    else:
        print(ans)