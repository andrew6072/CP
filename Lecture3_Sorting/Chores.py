n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

x = 0
gap = - h[b-1] + h[b]
if gap != 0:
    x = gap
print(x)
