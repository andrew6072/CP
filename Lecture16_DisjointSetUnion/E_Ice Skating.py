def findParent(parents, u):
    if u != parents[u]:
        parents[u] = findParent(parents, parents[u])
    return parents[u]


def unionSet(parents, ranks, u, v):
    pu = findParent(parents, u)
    pv = findParent(parents, v)
    if  pv == pu:
        return
    if ranks[pu] > ranks[pv]:
        parents[pv] = pu
    elif ranks[pu] < ranks[pv]:
        parents[pu] = parents[pv]
    else:
        parents[pu] = pv
        ranks[pv] += 1
    return


def isInSameSet(point1, point2):
    return point1[0] == point2[0] or point1[1] == point2[1]


def solve():
    n = int(input())
    parents = [i for i in range(n+1)]
    ranks = [0 for _ in range(n+1)]
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(n):
        for j in range(n):
            if i != j and isInSameSet(points[i], points[j]):
                unionSet(parents, ranks, i, j)

    ans = 0
    for i in range(n):
        if i == parents[i]:
            ans += 1

    print(ans - 1)


solve()
