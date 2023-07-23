n , x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
time = 0
for i in range(n):
    time += a[i] * x
    if x > 1:
        x -= 1

print(time)