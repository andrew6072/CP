def FloydWarshall(dist, n):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


INF = 10**9
tc = 1
while True:
    try:
        dist = [[INF for _ in range(20)] for _ in range(20)]
        for i in range(20):
            dist[i][i] = 0

        for i in range(1, 20):
            arr = list(map(int, input().split()))
            for x in arr[1:]:
                dist[i - 1][x - 1] = 1
                dist[x - 1][i - 1] = 1

        FloydWarshall(dist, 20)

        n = int(input())
        print(f'Test Set #{tc}')
        for _ in range(n):
            u, v = map(int, input().split())
            cost = dist[u - 1][v - 1]
            print(f"{u:2d} to {v:2d}: {cost:d}")

        tc += 1
        print()
    except EOFError:
        break
