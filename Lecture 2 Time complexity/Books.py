n , t = map(int, input().split())
a = list(map(int, input().split()))

max = 0
i, j = 0, 0
sum = 0
while(i < n and j < n):
    if (i == j and a[j] > t):
        sum = 0
        i += 1
        j += 1
    elif (sum + a[j] <= t):
        sum += a[j]
        count = j - i + 1
        if max < count:
            max = count
        j += 1
    else:
        sum -= a[i]
        i += 1

print(max)

# for i in range(n):
#     j = i
#     sum = 0
#     start = i
#     while (j < n and sum + a[j] <= t):
#         sum += a[j]
#         count = j - start + 1
#         if max < count:
#             max = count
#         j += 1
