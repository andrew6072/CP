n, w = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
min_girl = a[0]*1.0
min_boy = a[n]
half_min_boy = min_boy*1.0/2
cup_val = min(min_girl, half_min_boy)
x = w*1.0 / 3 / n
res = w
if cup_val < x:
    res = cup_val*3*n
print(res)