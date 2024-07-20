A = [0, 100]
container = []
ans = []
s = 0
max_sum = float('-inf')
for a in A:
    if a >= 0:
        s += a
        container.append(a)
        if s > max_sum:
            ans = container
            max_sum = s
        elif s == max_sum and len(container) > len(ans):
            ans = container
    else:
        container = []
        s = 0

print(ans)
