a = [0]*100005
n = int(input())
ans = 0
b = list(map(int, input().split()))

for i in range(1, n+1):
    k = b[i-1]
    a[k] = i
    if (a[k-1] > a[k+1]):
        ans = max(ans, i - max(a[k + 1], a[k - 2]))
    else:
        ans = max(ans, i - max(a[k + 2], a[k - 1]))

print(ans)