def BSFist(paired, arr, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or arr[mid - 1] < x or paired[mid - 1] == True) and x == arr[mid] and paired[mid] == False:
            paired[mid] = True
            return mid
        elif x > arr[mid] or (arr[mid] == x and paired[mid] == True):
            return BSFist(paired, arr, mid + 1, right, x)
        else:
            return BSFist(paired, arr, left, mid - 1, x)
    return -1


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    paired = [False for _ in range(n)]
    count = 0
    for i, x in enumerate(arr):
        if paired[i] != True:
            idx_target = BSFist(paired, arr, 0, n - 1, m - x)
            if idx_target != -1:
                paired[i] = True
                count += 1
    if n == 1:
        print(0)
    else:
        print(count)