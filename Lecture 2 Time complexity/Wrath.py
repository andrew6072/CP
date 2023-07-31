
# a = [1, 1, 3, 0, 0 ,0, 2 ,1 ,0, 3]
# a = [0 ,1 ,0 ,10]
# a = [0, 0]
# n = len(a)

n = int(input())
a = list(map(int, input().split()))

# b = [1]*n
# count = n
# for i in range(n-1, -1, -1):
#     l = a[i]
#     j = i
#     while l > 0 and j > 0:
#         if b[j - 1] == 1:
#             count -= 1
#         b[j - 1] = -1
#         j -= 1
#         l -= 1
l = 0
for i in range(n-1, -1, -1):
    if(l > 0):
        l -= 1
        l = max(l, a[i])
        a[i] = -1
    l = max(l, a[i])
count = 0
for i in range(n):
    if a[i] != -1:
        count += 1
print(count)


