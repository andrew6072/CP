n = int(input())
a = list(map(int, input().split()))
min_diff = 10**17
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            min_diff = min(a[i]-a[j], min_diff)
print(min_diff)
