n = int(input())
a = list(map(int, input().split()))

def solve(a, n):
    is_sorted = 1
    for k in range(1, n):
        if (a[k] < a[k-1]):
            is_sorted = -1
            break
    if (is_sorted == 1):
        print('yes')
        print(1, 1)
    else:
        sa = sorted(a)
        i, j = 0, n-1

        while (sa[i] == a[i] or sa[j] == a[j]):
            if (sa[i] == a[i]):
                i += 1
            if (sa[j] == a[j]):
                j -= 1

        left, right = i+1, j+1
        can = 1
        while j > i:
            if a[j-1] < a[j]:
                print('no')
                can = -1
                break
            j -= 1

        if can != -1:
            print('yes')
            print(left, right)

if n == 1:
    print('yes')
    print(1, 1)
elif n == 2:
    print('yes')
    if a[0] > a[1]:
        print(1, 2)
    else:
        print(1, 1)
else:
    solve(a, n)
