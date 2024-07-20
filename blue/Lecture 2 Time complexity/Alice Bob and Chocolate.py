n = int(input())
a = list(map(int, input().split()))
raw_a = [a[i] for i in range(n)]
i, j ,m = 0, n-1, n
A, B = 0, 0

while i <= j and m != 0:
    alice = a[i]
    bob = a[j]
    if (alice > bob and i != j - 1):
        a[i] -= a[j]
        m -= 1
        B += 1
        j -= 1
    elif (a[j] > a[i] and j != i + 1):
        a[j] -= a[i]
        m -= 1
        A += 1
        i += 1
    else:
        if (m != 1):
            A += 1
            B += 1
            m -= 2
            i += 1
            j -= 1
        else:
            i += 1
            A += 1
            m -= 1

print(A, B)