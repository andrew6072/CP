n, k = map(int, input().split())
arr = []
for i in range(n):
    a = input()
    arr.append(len(a))
password = input()
target = len(password)

arr.sort()

# k = 2
# arr = [1,1,2,2,2,3,3,3,3,4]
# n = len(arr)
# target = 4

best = 0
worst = 0
tries = 1
time = 1
index_target = 0

for i in range(n):
    if arr[i] == target:
        best = time
        index_target = i + 1
        break
    else:
        if (tries == k):
            time += 5 + 1 # add 1 as considering the entering time (1s)
            tries = 1
        else:
            tries += 1
            time += 1

i = index_target
while (i < n):
    if (arr[i] == target):
        if (tries == k):
            time += 5 + 1 # add 1 as considering the entering time (1s)
            tries = 1
        else:
            tries += 1
            time += 1
        i += 1
    else:
        break


worst = time
print(best, worst)