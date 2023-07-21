import heapq

N = int(input())
minHeap = []
maxHeap = []
count = 0
for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] == 1:
        # test method
        heapq.heappush(maxHeap, -a[1]) #O(log(n))
        count += 1
        if len(minHeap) > 0 and -maxHeap[0] > minHeap[0]: #O(log(n))
                v1 = -heapq.heappop(maxHeap)
                v2 = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -v2)
                heapq.heappush(minHeap, v1)

        # second method
        # if len(minHeap) > 0 and minHeap[0] < a[1]: #O(log(n))
        #     heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        #     heapq.heappush(minHeap, a[1])
        # else:
        #     heapq.heappush(maxHeap, -a[1]) #O(log(n))
        # count += 1

        if count % 3 == 0:
            v = -1 * heapq.heappop(maxHeap)
            heapq.heappush(minHeap, v)
    else:
        if count < 3:
            print('No reviews yet')
        else:
            print(minHeap[0])
