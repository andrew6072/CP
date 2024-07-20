def check(arr, x):
    sum = 0
    for a in arr:
        if a > x:
            sum += a - x
    return sum

n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_val = max(arr)
left = 0
right = max_val
ans = -1
while left <= right:
    mid = (left + right)//2
    if check(arr, mid) > m:
        ans = mid
        left = mid + 1
    elif check(arr, mid) < m:
        right = mid - 1
    else:
        ans = mid
        break
print(ans)