import queue

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    q = queue.Queue()
    for i in range(len(a)-1, -1, -1):
        q.put((a[i], i))
    count = 0
    j = len(a)-1
    while not q.empty() and q.queue[0][1] != m:
        while q.queue[0][0] != sorted_a[j]:
            x = q.get()
            q.put(x)
            count += 1
        j -= 1
        q.get()
        count += 1
    print(count+1)