import queue

INF = int(2*10e5+5)
MAX = int(10e4)

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
        for neighbor in graph[u]:
            if w + neighbor.cost < dist[neighbor.idx]:
                dist[neighbor.idx] = w + neighbor.cost
                pq.put(Node(neighbor.idx, dist[neighbor.idx]))


def findIdCity(name, name_list):
    idx = -1
    for i in range(len(name_list)):
        if name_list[i] == name:
            idx = i
    return idx


tc = int(input())
for _ in range(tc):
    #input
    n = int(input())
    no = 1
    graph = [[] for _ in range(MAX + 5)]
    name_list = []
    name_list.append('city0')
    for _ in range(n):
        name = input()
        name_list.append(name)
        p = int(input())
        for _ in range(p):
            nr, cost = map(int, input().split())
            graph[no].append(Node(nr, cost))
        no += 1

    # output
    r = int(input())
    for _ in range(r):
        dist = [INF] * (MAX + 5)
        city1, city2 = input().split()
        idx1, idx2 = findIdCity(city1, name_list), findIdCity(city2, name_list)
        Dijkstra(graph, dist, idx1)
        print(dist[idx2])
    input()

