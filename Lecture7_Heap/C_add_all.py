import heapq

n = -1
while n != 0:
    n = int(input())
    if n != 0:
        h = list(map(int, input().split()))
        heapq.heapify(h) # O(n)
        sum = 0
        cost = 0
        while len(h) > 1: # O(n)
            sum = heapq.heappop(h) + heapq.heappop(h) # O(2 * log(n))
            heapq.heappush(h, sum) # O(log(n))
            cost += sum
        print(cost)

# Time complexity: O(n*log(n))