import math
import queue

INF = 10e9


class Node:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def __lt__(self, other):
        return self.cost <= other.cost

    def __repr__(self):
        return f"({self.id}, {self.cost})"


def lengthPoints(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def prims(graph, path, visited, dist, src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    while pq.empty() == False:
        top = pq.get()
        u = top.id
        visited[u] = True

        if top.cost != dist[u]:
            continue

        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.cost
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


def printMST(dist, path, n):
    ans = 0
    for i in range(n + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans


while True:
    try:
        n = int(input())
        graph = [[] for _ in range(n + 1)]
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        m = int(input())
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(Node(v, 0))
            graph[v].append(Node(u, 0))

        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                if i != j:
                    graph[i + 1].append(Node(j + 1, lengthPoints(point1, point2)))
                    graph[j + 1].append(Node(i + 1, lengthPoints(point1, point2)))

        dist = [INF for _ in range(n + 1)]
        path = [-1 for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]

        prims(graph, path, visited, dist, 1)
        print("%.2f" % printMST(dist, path, n))

    except EOFError:
        break