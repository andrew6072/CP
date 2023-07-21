t = int(input())
for _ in range(t):
    N = int(input())
    cost = 0
    for _ in range(N):
        a, b, d = map(int, input().split())
        if b <= d:
            continue
        if b > d:
            if d == 0:
                cost += (b*1.0)/a
            else:
                cost += (b-d)*1.0/a
    print("%.2f" % cost)
