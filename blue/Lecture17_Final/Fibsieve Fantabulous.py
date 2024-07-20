import math

t = int(input())

for tt in range(1, t + 1):
    s = int(input())
    print(f"Case {tt}: ", end="")
    root = int(math.sqrt(s))

    if root * root == s and root % 2 == 1:
        print(f"1 {root}")
        continue
    if root * root == s and root % 2 == 0:
        print(f"{root} 1")
        continue

    if root % 2 == 0:
        r = root + 1
        ind = r * r

        if s >= ind - r + 1:
            c = ind - s + 1
        else:
            c = root + 1
            minus = ind - r + 1 - s
            r -= minus

        print(f"{c} {r}")

    else:
        ind = (root + 1) * (root + 1)
        f = root + 1
        if s >= ind - f + 1:
            c = f
            plus = ind - s
            r = plus + 1
        else:
            r = f
            q = ind - f + 1 - s
            c = f - q
        print(f"{c} {r}")
