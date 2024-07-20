def bs(a, left, right, x):
    if left <= right:
        mid = (left+right)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            return bs(a, mid + 1, right, x)
        else:
            return bs(a, left, mid - 1, x)
    return -1


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
for x in a:
    if bs(a, 0, n-1, x-k) != -1:
        count += 1
    if bs(a, 0, n-1, x+k) != -1:
        count += 1
print(count//2)
