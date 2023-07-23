'''
3
USDollar
BritishPound
FrenchFranc
3
USDollar 0.5 BritishPound
BritishPound 10.0 FrenchFranc
FrenchFranc 0.21 USDollar

3
USDollar
BritishPound
FrenchFranc
6
USDollar 0.5 BritishPound
USDollar 4.9 FrenchFranc
BritishPound 10.0 FrenchFranc
BritishPound 1.99 USDollar
FrenchFranc 0.09 BritishPound
FrenchFranc 0.19 USDollar

0
'''
def FloydWarshall(dist, n):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][j] < dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]
    for i in range(n):
        if dist[i][i] > 1.0:
            return True
    return False


INF = -10**9

n = -1
tc = 1
while n != 0:
    n = int(input())
    if n != 0:
        graph = [[INF for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][j] = 1.0


        nodes = []
        node_to_idx = {}
        for i in range(n):
            currency = input()
            nodes.append(currency)
            node_to_idx.update({currency: i})

        m = int(input())
        for _ in range(m):
            curr1, rate, curr2 = input().split()
            u = node_to_idx[curr1]
            v = node_to_idx[curr2]
            r = float(rate)
            graph[u][v] = r
        input()

        ans = FloydWarshall(graph, n)
        if ans:
            print(f'Case {tc}: Yes')
        else:
            print(f'Case {tc}: No')
        tc += 1