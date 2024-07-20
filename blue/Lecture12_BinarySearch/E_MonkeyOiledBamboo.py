def check(n, arr, k):
    if k < arr[0]:
        return False
    for i in range(1, n):
        if k < arr[i] - arr[i - 1]:
            return False
        if k == arr[i] - arr[i - 1]:
            k -= 1
    return True

tc = int(input())
for i in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    left = 1
    right = arr[n-1]
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if check(n, arr, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(f'Case {i + 1}: {ans}')
