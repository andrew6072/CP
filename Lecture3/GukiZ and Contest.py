n = int(input())
a = list(map(int, input().split()))

sa = sorted(a, reverse=True)
level_sa = [1]*n
rank = [0]*2005
rank[sa[0]] = 1
level = 2

for i in range(1, n):
    if sa[i] == sa[i-1]:
        level_sa[i] = level_sa[i-1]
    else:
        level_sa[i] = level
        rank[sa[i]] = level_sa[i]
    level += 1

for i in range(n):
    print(rank[a[i]], end=' ')