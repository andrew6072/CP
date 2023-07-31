n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# n, m = 20, 25
# a = [30, 32, 34, 39, 42, 43, 45, 46, 47, 48, 52, 55, 56, 57, 58, 59, 60, 65, 67, 69]
# b = [2, 3, 4, 5, 8, 9, 14, 16, 18, 20, 24, 27, 29, 30, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46]
a.sort()
b.sort()

index_a = 0
index_b = 0
more = n
while (index_a < n and index_b < m):
    if (a[index_a] <= b[index_b]):
        index_a += 1
        index_b += 1
        more -= 1
    else:
        index_b += 1

print(more)
# upper_bound = 10**6 + 1
# cnt_b = [0 for _ in range(1, upper_bound)]
# more = 0
#
# for x in b:
#     cnt_b[x] += 1
#
# not_match = []
#
# for x in a:
#     if(cnt_b[x] == 0):
#         not_match.append(x) # this x is in a but cannot be found in b
#         more += 1
#     else:
#         cnt_b[x] -= 1
#         if cnt_b[x] == 0:
#
#
#
# for x in not_match:
#
# print(more)