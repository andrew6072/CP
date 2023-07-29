import math

def f(p , q , r , s , t , u , x):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u

while True:
    try:
        p, q, r, s, t, u = map(int, input().split())
        left = 0
        right = 1
        mid = -1
        while right - left > 10**-8:
            mid = (right+left)/2
            if f(p, q, r, s, t, u, mid) < 0: # need bigger f(x), so decrease x
                right = mid
            elif f(p, q, r, s, t, u, mid) > 0:
                left = mid
            else:
                break
        res = abs(f(p, q, r, s, t, u, mid))
        if res < 10**-4:
            print("%.4f" % mid)
        else:
            print('No solution')
    except EOFError:
        break