def bsLast(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == right or a[mid + 1] >= x) and a[mid] < x:
            return mid
        elif a[mid] >= x:
            return bsLast(a, left, mid - 1, x)
        else:
            return bsLast(a, mid + 1, right, x)
    return -1


def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or a[mid - 1] <= x) and a[mid] > x:
            return mid
        elif a[mid] <= x:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = list(map(int, input().split()))
for x in queries:
    first_bigger = bsFirst(a, 0, n - 1, x)
    last_smaller = bsLast(a, 0, n - 1, x)
    ans1 = a[last_smaller]
    ans2 = a[first_bigger]
    if last_smaller == -1:
        ans1 = 'X'
    if first_bigger == -1:
        ans2 = 'X'
    print(ans1, ans2)
