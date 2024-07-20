n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# while (i < n and j < m):
#     if (a[i] - x <= b[j] and b[j] <= a[i] + y):
#         j += 1
#         i += 1
#         k += 1
#         soldier.append(i)
#         vest.append(j)
#     else:
#         i += 1
cnt = 0
j = 0
c = [0] * 100005
d = [0] * 100005

for i in range(n):
    while j < m and a[i] - x > b[j]:
        j += 1

        
    if j == m:
        break
    if a[i] + y >= b[j]:
        c[cnt] = i + 1
        d[cnt] = j + 1
        cnt += 1
        j += 1

print(cnt)
for i in range(cnt):
    print(c[i], d[i])
