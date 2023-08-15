def findSet(parent, u):
    if parent[u] != u:
        parent[u] = findSet(parent, parent[u])
    return parent[u]


def sameSet(parent, u, v):
    return findSet(parent, u) == findSet(parent, v)


def unionSet(parent, ranks, u, v):
    up = findSet(parent, u)
    vp = findSet(parent, v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


m, n = -1, -1
tc = 1
while m != 0 and n !=0:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+5)]
    ranks = [0 for _ in range(n+5)]
    paired = [False for _ in range(n+5)]
    num_paired = 0
    for _ in range(m):
        u, v = map(int, input().split())
        unionSet(parent, ranks, u, v)
        if paired[u] == False:
            num_paired += 1
            paired[u] = True
        if paired[v] == False:
            num_paired += 1
            paired[v] = True

    num_set = 0
    for i in range(1, n+1):
        if i == parent[i]:
            num_set += 1
    print(f'Case {tc}: {num_set}')
    tc += 1
