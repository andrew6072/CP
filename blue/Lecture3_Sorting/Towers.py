n = int(input())
a = list(map(int, input().split()))

a.sort()
high, max_high, tower = 1, 1, 1

for i in range(1, n):
    if (a[i] != a[i-1]):
        tower += 1
        high = 1
    else:
        high += 1
        max_high = max(max_high, high)

print(max_high, tower)