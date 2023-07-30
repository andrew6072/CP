import math

n, s = map(int, input().split())
radius_pop = {}
for _ in range(n):
    x, y, k = map(int, input().split())
    r = math.sqrt(x**2 + y**2)
    if not (r in radius_pop):
        radius_pop[r] = k
    else:
        radius_pop[r] += k
if s >= 10**6:
    print(0)
else:
    sorted_dict = dict(sorted(radius_pop.items(), key=lambda item: item[0]))
    min_radius_needed = -1
    for radius in sorted_dict.keys():
        s += sorted_dict[radius]
        if s >= 10**6:
            min_radius_needed = radius
            break
    if min_radius_needed != -1:
        print('%.7f' % min_radius_needed)
    else:
        print(-1)
