# import heapq
#
#
# def findLargest(h):
#     largest = -1
#     for x in h:
#         if x > largest:
#             largest = x
#     return largest
#
#
# cost = 0
# n = int(input())
# h = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     k = a[0]
#     for i in range(1, k+1): # O(k*log(k))
#         heapq.heappush(h, a[i])
#
#     smallest = h[0]
#     largest = findLargest(h) # O(n*k)
#     cost += (largest - smallest)
#     heapq.heappop(h) # O(log(n*k))
#     h.remove(largest) # O(n*k)
#     heapq.heapify(h) # O(n*k)
#
# print(cost)
import heapq


def getPromotion(minHeap, maxHeap, deletedMin, deletedMax, arr):
    for a in arr:
        heapq.heappush(minHeap, a)
        heapq.heappush(maxHeap, -a)
    while deletedMin[minHeap[0]] > 0: # O(N/2*log(N/2)) but it just runs one time in worst case
        deletedMin[minHeap[0]] -= 1
        heapq.heappop(minHeap) # O(log(n*k))
    while deletedMax[-maxHeap[0]] > 0:
        deletedMax[-maxHeap[0]] -= 1
        heapq.heappop(maxHeap)
    if len(minHeap) > 1:
        top_min = minHeap[0]
        top_max = -maxHeap[0]
        deletedMin[top_max] += 1
        deletedMax[top_min] += 1
        heapq.heappop(minHeap) # O(log(n*k))
        heapq.heappop(maxHeap) # O(log(n*k))
        return top_max - top_min
    return 0

n = int(input())
cost = 0
minHeap = []
maxHeap = []
deletedMin = [0] * 1000001
deletedMax = [0] * 1000001
for _ in range(n):
    arr = list(map(int, input().split()))
    cost += getPromotion(minHeap, maxHeap, deletedMin, deletedMax, arr[1:arr[0]+1])
    # in worst case this for loop runs at O(nlog(N/2)) to delete all first half of the heaps
    # after deleting all first half, we're left with the other half, this part can be deleted
    # in O(N/2*log(N/2)) so the total time complexity is O(nlog(N/2)) + O(N/2*log(N/2)) ~ O(Nlog(N))
print(cost)
