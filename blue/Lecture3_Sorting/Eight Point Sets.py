class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr((self.x, self.y))

def count_point(array_points):
    fre_x = [0] * (10 ** 6 + 5)
    fre_y = [0] * (10 ** 6 + 5)
    cnt_x = 0
    cnt_y = 0
    for point in array_points:
        if (fre_x[point.x] == 0):
            cnt_x += 1
            fre_x[point.x] += 1
        else:
            fre_x[point.x] += 1

        if (fre_y[point.y] == 0):
            cnt_y += 1
            fre_y[point.y] += 1
        else:
            fre_y[point.y] += 1
    return cnt_x, cnt_y, fre_x, fre_y



array_points = []
for i in range(8):
    x, y = map(int, input().split())
    array_points.append(Point(x, y))

cnt_x, cnt_y, fre_x, fre_y = count_point(array_points)

if cnt_x != 3 or cnt_y != 3:
    print('ugly')
else:
    a = sorted(array_points, key=lambda s: (s.y, s.x))
    if (a[4].x != a[2].x):
        print('ugly')
    else:
        res = 'respectable'
        fre_x1, fre_y1 = fre_x[a[0].x], fre_y[a[0].y]
        fre_x2, fre_y2 = fre_x[a[1].x], fre_y[a[3].y]
        fre_x3, fre_y3 = fre_x[a[7].x], fre_y[a[7].y]
        if not(fre_x1 == 3 and fre_y1 == 3 and fre_x2 == 2 and fre_y2 == 2 and fre_x3 == 3 and fre_y3 == 3):
            res = 'ugly'
        print(res)