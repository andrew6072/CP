tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    student_num_candy = {}
    for i in range(n):
        student_num_candy[a[i]] = 1
    for i in range(n, n+m):
        if a[i] in student_num_candy:
            print('YES')
        else:
            print('NO')
            student_num_candy[a[i]] = 1
