n = int(input())
a = list(map(int, input().split()))
ps = [a[0]]
for i in range(1, n):
    ps.append(ps[i-1] + a[i])
print(ps)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    minus = ps[l-1]
    if l - 1 < 0:
        minus = 0
    cnt1 = ps[r] - minus
    sumXor = cnt1 % 2
    cnt0 = (r-l+1) - cnt1
    print(sumXor, cnt0)
    print()