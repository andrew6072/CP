n, k = map(int, input().split())
a = list(map(int, input().split()))
# n, k = 50, 7
# a = [2, 5, 6, 5, 2, 1, 7, 9, 7, 2, 5, 5, 2, 4, 7, 6, 2, 2, 8, 7, 7, 9, 8, 1, 9, 6, 10, 8, 8, 6, 10, 3, 3, 9, 1, 10, 5, 8, 1, 10, 7, 8, 4, 8, 6, 5, 1, 10, 2, 5]


def sliceToLastUnique(index, a):
    while (index < len(a) - 1 and a[index] == a[index+1]):
        index += 1
    return index

def getDistinctArray(a, k, index):
    apperance = [False for _ in range(0, 100001)]
    a_index = a[index]
    apperance[a_index] = True
    k -= 1
    i = index + 1

    while k > 0 and i < len(a):
        current = a[i]
        previous = a[i-1]
        if (current != previous and apperance[current] == False):
            k -= 1
            apperance[current] = True
        i += 1

    if (k != 0):
        return -1, -1
    return index, i-1

def solve(a, k):
    index = sliceToLastUnique(0, a)
    left, right = getDistinctArray(a, k, index)
    if (left != -1 and right != -1):
        cnt_dA = [0 for _ in range(0, 100001)]
        for i in range(left, right+1):
            cnt_dA[a[i]] += 1
        i = left
        while (cnt_dA[a[i]] > 1):
            cnt_dA[a[i]] -= 1
            i += 1
        left = i + 1
        right = right + 1

    print(left, right)

solve(a, k)


# left, right = solve(a, k)
# print(left, right)