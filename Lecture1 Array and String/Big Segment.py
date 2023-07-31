n = int(input())
left = []
right = []
for i in range(n):
    a, b = map(int, input().split())
    left.append(a)
    right.append(b)

min_left = 10e09
max_right = 1

for i in range(n):
    if left[i] < min_left:
        min_left = left[i]
    if right[i] > max_right:
        max_right = right[i]

found = 0
for i in range(n):
    if(left[i] == min_left and right[i] == max_right):
        print(i+1)
        found = 1
        break

if found == 0:
    print(-1)