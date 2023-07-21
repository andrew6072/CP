import heapq


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1 # equals to (pos - 1)//2
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def removeNumFromHeap(heap, element): # O(n)
    idx = heap.index(element)  # find the element O(n)
    heap[idx] = heap[-1]  # replace the last to the element to be deleted
    del heap[-1]  # delete the last element

    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if idx < len(heap):
        _siftup(heap, idx) # O(log(n))
        _siftdown(heap, 0, idx) # O(log(n))


V = []
for _ in range(int(input())):
    command = list(map(int, input().split()))
    if command[0] == 1:
        heapq.heappush(V, command[1])
    elif command[0] == 2:
        removeNumFromHeap(V, command[1])
    elif command[0] == 3:
        print(V[0])