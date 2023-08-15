import math
import queue

INF = 10**9


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


def solve(points, n):
    graph = [[] for _ in range(n+5)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append(Node(j, lengthPoints(points[i], points[j])))
                graph[j].append(Node(i, lengthPoints(points[i], points[j])))

    dist = [INF for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    prims(graph, path, visited, dist, 0)
    return printMST(dist, path, n)


tc = int(input())
input()
for i in range(tc):
    points = []
    n = int(input())
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))
    if i != tc - 1:
        input()
    ans = solve(points, n)
    print("%.2f" % ans)
    if i != tc - 1:
        print()