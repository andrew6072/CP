n = int(input())
a = list(map(int, input().split()))

turn = 1
S = 0
D = 0
left = 0
right = n - 1
pick = 0
while (left <= right):
    if (a[left] >= a[right]):
        pick = a[left]
        left += 1
    else:
        pick = a[right]
        right -= 1
    if turn == 1:
        S += pick
    else:
        D += pick

    turn *= -1

print(S, D)