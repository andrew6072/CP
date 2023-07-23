def solve(data, n):
    s_data = sorted(data)
    s = []
    res = []
    i = 0
    j = 0
    while j < n:
        if data[i] == s_data[j]:
            res.append(data[i])
            if i != n - 1:
                i += 1
            j += 1
        else:
            if len(s) == 0:
                s.append(data[i])
            else:
                if s[-1] != s_data[j] and i != n - 1:
                    s.append(data[i])
                    if i != n - 1:
                        i += 1
                else:
                    res.append(s.pop())
                    j += 1


    ans = 'yes'
    for i in range(n):
        if res[i] != s_data[i]:
            ans = 'no'
            break
    print(ans)

# n = 20
# data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

n = -1
while n != 0:
    n = int(input())
    if n != 0:
        data = list(map(int, input().split()))
        solve(data, n)

