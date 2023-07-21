k = int(input())
a = list(map(int, input().split()))

if k == 0:
    print(0)
else:
    n = len(a)
    a = sorted(a, reverse=True)

    count = 0
    growth = 0
    for i in range(n):
        if (growth >= k):
            break
        else:
            growth += a[i]
            count += 1
    if growth < k:
        print(-1)
    else:
        print(count)