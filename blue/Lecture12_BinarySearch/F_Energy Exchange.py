def SumLost(k, m, arr):
    sum = 0
    for a in arr:
        if a > m:
            sum += a - m
    return sum * k / 100


n, k = map(int, input().split())
arr = list(map(int, input().split()))
initial_sum = sum(arr)
left = 0
right = 1000
mid = -1
while right - left > 10**-7:
    mid = (right+left)/2
    sum_lost = SumLost(k, mid, arr)
    if mid * n < initial_sum - sum_lost:
        left = mid
    elif mid * n > initial_sum - sum_lost:
        right = mid
    else:
        break

print("%.9f" % mid)