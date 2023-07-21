import heapq


class PQEntry:
    def __init__(self, id, old, new):
        self.id = id
        self.old = old
        self.new = new

    def getIncrement(self):
        return self.new - self.old

    def __lt__(self, other):
        if self.getIncrement() != other.getIncrement():
            return self.getIncrement() > other.getIncrement()
        else:
            return self.id > other.id

def newScore(posts, likes, cmts, shares):
    return 50*posts + 5*likes + 10*cmts + 20*shares

h = []
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    heapq.heappush(h, PQEntry(a[0], a[1], newScore(a[2], a[3], a[4], a[5])))

count = 0
while len(h) > 0 and count < 5:
    count += 1
    topic = heapq.heappop(h)
    print(topic.id, topic.new)