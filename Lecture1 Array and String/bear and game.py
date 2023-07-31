n = int(input())
hot = list(map(int, input().split()))
#16, 20, 30, 40, 50, 60, 70, 80, 90 -> 15
#15, 20, 30, 40, 50, 60, 70, 80, 90 -> 90
#7, 20, 88 -> 35
j = 0
boring = 0
i = 0
while i < 90:
    if (i == hot[j]):
        if j != (n - 1):
            j += 1
        boring = 1
    else:
        if (boring == 15):
            break
        else:
            boring += 1
    i += 1

print(i)

