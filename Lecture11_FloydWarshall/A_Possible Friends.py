INF = 10**9


def FloydWarshall(graph, dist, n):
    for i in range(n):
        for j in range (n):
            if graph[i][j] == 'Y':
                dist[i][j] = 1
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


T = int(input())

for _ in range(T):
    graph = []
    line1 = list(input().strip())
    n = len(line1)
    graph.append(line1)
    for _ in range(n - 1):
        line_i = list(input().strip())
        graph.append(line_i)
    dist = [[INF for _ in range(n)] for _ in range(n)]
    FloydWarshall(graph, dist, n)
    ans = (-1, -1)
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and dist[i][j] == 2:
                count += 1
        if count > ans[1]:
            ans = (i, count)
    print(ans[0], ans[1])
