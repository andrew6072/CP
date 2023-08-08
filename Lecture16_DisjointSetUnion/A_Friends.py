def findSet(parent, u):
    if parent[u] != u:
        parent[u] = findSet(parent, parent[u])
    return parent[u]


def unionSet(num, ranks, parent, u, v):
    up = findSet(parent, u)
    vp = findSet(parent, v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        num[up] += num[vp]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        num[vp] += num[up]
    else:
        parent[up] = vp
        ranks[vp] += 1
        num[vp] += num[up]


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 5)]
    ranks = [0 for _ in range(n + 5)]
    num = [1 for _ in range(n + 5)]
    for _ in range(m):
        u, v = map(int, input().split())
        unionSet(num, ranks, parent, u, v)
    print(max(num))



