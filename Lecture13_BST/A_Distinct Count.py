tc = int(input())
for _ in range(tc):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a)
    if len(s) == x:
        print('Good')
    else:
        if len(s) < x:
            print('Bad')
        else:
            print('Average')
