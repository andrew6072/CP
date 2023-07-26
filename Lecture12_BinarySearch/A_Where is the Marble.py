def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


tc = 1
n, q = -1, -1
while n != 0 and q != 0:
    n, q = map(int, input().split())
    if n != 0 and q != 0:
        arr = []
        for _ in range(n):
            x = int(input())
            arr.append(x)
        arr.sort()

        print(f'CASE# {tc}:')
        for _ in range(q):
            x = int(input())
            res = bsFirst(arr, 0, len(arr) - 1, x)
            if res != -1:
                print(f'{x} found at {res + 1}')
            else:
                print(f'{x} not found')
        tc += 1
