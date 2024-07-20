class Heap:
    def __init__(self):
        self.h = []

    def __str__(self):
        return f'{self.h}'

    def getLen(self):
        return len(self.h)

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.h):
            if self.h[left] < self.h[smallest]:
                smallest = left
        if right < len(self.h):
            if self.h[right] < self.h[smallest]:
                smallest = right
        if i != smallest:
            self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
            self.heapify(smallest)

    def getPeek(self):
        return self.h[0]

    def buildHeap(self, len, A):
        self.h = A
        for i in range(len//2 - 1, -1, -1):
            self.heapify(i)

    def put(self, value):
        self.h.append(value)
        i = self.getLen() - 1
        while i != 0 and self.h[(i-1)//2] > self.h[i]:
            self.h[(i-1)//2], self.h[i] = self.h[i], self.h[(i-1)//2]
            i = (i-1)//2

    def pop(self):
        n = len(self.h)
        if n == 0:
            return
        self.h[0] = self.h[n - 1]
        self.h.pop()
        self.heapify(0)

    # def remove(self, value):
    #     n = len(self.h)
    #     if n == 0:
    #         return
    #     i = 0
    #     while i < n and self.h[i] != value:
    #         i += 1
    #     self.h[i] = self.h[n - 1]
    #     self.h.pop()
    #     self.heapify(i)

    def _siftdown(self, startpos, pos):
        newitem = self.h[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1  # equals to (pos - 1)//2
            parent = self.h[parentpos]
            if newitem < parent:
                self.h[pos] = parent
                pos = parentpos
                continue
            break
        self.h[pos] = newitem

    def _siftup(self, pos):
        endpos = len(self.h)
        startpos = pos
        newitem = self.h[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2 * pos + 1  # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.h[childpos] < self.h[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.h[pos] = self.h[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.h[pos] = newitem
        self._siftdown(startpos, pos)

    def removeNumFromHeap(self, element):  # O(n)
        idx = self.h.index(element)  # find the element O(n)
        self.h[idx] = self.h[-1]  # replace the last to the element to be deleted
        del self.h[-1]  # delete the last element

        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if idx < len(self.h):
            self._siftup(idx)  # O(log(n))
            self._siftdown(0, idx)  # O(log(n))


# heap = Heap()
# A = [7,12,6,10,17,15,2,4]
# heap.buildHeap(len(A), A)
# print(heap)
# heap.put(3)
# print(heap)
# heap.pop()
# print(heap)
# heap.remove(6)
# print(heap)

q = int(input())
heap = Heap()
ans = []
for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] == 3:
        print(heap.getPeek())
        ans.append(heap.getPeek())
    elif a[0] == 1:
        heap.put(a[1])
    elif a[0] == 2:
        heap.removeNumFromHeap(a[1])