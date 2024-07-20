n = int(input())
arr = list(map(int, input().split()))
a = []
for i in range(n):
    x = arr[i]
    a.append((x, i))
a.sort()

c = 0

def swapTuple(tup1, tup2):
    new_tup1 = (tup1[0], tup2[1])
    new_tup2 = (tup2[0], tup1[1])
    return new_tup1, new_tup2

for i in range(n - 1):
    if a[i][0] == a[i + 1][0]:
        c += 1
    if c == 2:
        print("YES")
        for j in range(n):
            print(a[j][1] + 1, end=" ")
        print()
        c = 0
        for j in range(n - 1):
            if a[j][0] == a[j + 1][0]:
                c += 1
                #a[j][1], a[j + 1][1] = a[j + 1][1], a[j][1]
                new_aj, new_aj1 = swapTuple(a[j], a[j+1])
                a[j] = new_aj
                a[j+1] = new_aj1

                for k in range(n):
                    print(a[k][1] + 1, end=" ")
                print()
                #a[j][1], a[j + 1][1] = a[j + 1][1], a[j][1]
                new_aj, new_aj1 = swapTuple(a[j], a[j + 1])
                a[j] = new_aj
                a[j + 1] = new_aj1
            if c == 2:
                exit(0)

print("NO")
