#a = [5,4,5,5,6,7,8,8,8,7,6]
# a = [2,2,1,2,2,1,2,2,3,3,2,3]
#a = [1,2,3,3,2]
#n = len(a)

n = int(input())
a = list(map(int, input().split()))

def findIntervalMaxMin(a, start_index):
    index_diff = start_index
    for i in range(start_index+1, n):
        if(abs(a[i]-a[i-1]) != 0):
            index_diff = i
            break
    if (a[start_index] > a[index_diff]):
        max = a[start_index]
        min = a[index_diff]
    else:
        min = a[start_index]
        max = a[index_diff]
    return min, max, index_diff

def findLength(a,start_index):
    count = 0
    min, max, index_diff = findIntervalMaxMin(a, start_index)
    last_index_diff = index_diff
    for i in range(start_index, n):
        if (abs(a[i] - min) > 1 or abs(a[i]-max) > 1):
            break
        else:
            if(a[i] - a[index_diff] == 0):
                last_index_diff = i
            count += 1
    return count, last_index_diff

start_index = 0
max_len = 0
while start_index < n:
    len, last_index_diff = findLength(a, start_index)
    if (len > max_len):
        max_len = len
    #start_index = last_index_diff
    start_index += 1

print(max_len)