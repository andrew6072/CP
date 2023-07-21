import queue

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value


pq = queue.PriorityQueue()

N = int(input())
A = list(map(int, input().split()))


for i in range(N):
    pq.put(PQEntry(A[i]))
    if i < 2:
        print(-1)
    else:
        max1 = pq.get().value
        max2 = pq.get().value
        max3 = pq.get().value
        print(max3 * max2 * max1)
        pq.put(PQEntry(max1))
        pq.put(PQEntry(max2))
        pq.put(PQEntry(max3))