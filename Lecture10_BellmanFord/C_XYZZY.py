class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    def __str__(self):
        return f'({self.source}, {self.target}, {self.weight})'

def BellmanFord(n, m, path, dist, graph, s):
    dist[s] = 0
    relaxed = True
    for _ in range(n-1):
        if relaxed == False:
            break
        relaxed = False
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] <= -100:
                continue
            if (dist[u] != INF) and (dist[u] + w > dist[v]):
                path[v] = u
                dist[v] = dist[u] + w
                relaxed = True

    for _ in range(n-1):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] <= -100:
                continue
            if (dist[u] != INF) and (dist[u] + w > dist[v]):
                dist[v] = -INF


INF = -10**14
n = -2
while n != -1:
    n = int(input())
    if n != -1:
        graph = []
        inp = []

        for _ in range(n-1):
            a = list(map(int, input().split()))
            inp.append(a)
        input()

        inp.append([0, 0, 0])
        for i, arr in enumerate(inp):
            for x in arr[2:]:
                next_room_energy = inp[x-1][0]
                graph.append(Edge(i+1, x, next_room_energy))
        graph.pop()

        m = len(graph)
        dist = [INF for _ in range(n+1)]
        path = [-1 for _ in range(n+1)]

        BellmanFord(n, m, path, dist, graph, 1)
        energy_point_in_the_path = dist[n]
        # trace back by path array to determine if there is a positive loop


        if (energy_point_in_the_path > -100):
            print('winnable')
        else:
            it = n
            have_infinite_loop = False
            while it != -1 and it != 1:
                if dist[it] == -INF:
                    have_infinite_loop = True
                it = path[it]
            if have_infinite_loop:
                print('winnable')
            else:
                print('hopeless')