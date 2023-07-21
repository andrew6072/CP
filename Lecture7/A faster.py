N = int(input())
A = list(map(int, input().split()))
max1, max2, max3 = -1, -2, -3
for i in range(N):
    if max3 < A[i] and A[i] <= max2:
        max3 = A[i]
    elif max2 < A[i] and A[i] <= max1:
        max3 = max2
        max2 = A[i]
    elif max1 < A[i]:
        max3 = max2
        max2 = max1
        max1 = A[i]
    if i < 2:
        print(-1)
    else:
        print(max3*max2*max1)