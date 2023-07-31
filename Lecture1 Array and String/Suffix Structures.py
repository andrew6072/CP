s = input()
t = input()

# def findInArray(x, a):
#     for i in range(len(a)):
#         if a[i] == x:
#             a[i] = -1
#             return True
#     return False
#
# def processString(s, t):
#     arr_s = toArray(s)
#     arr_t = toArray(t)
#     for i in range(len(arr_s)):
#         if findInArray(arr_s[i], arr_t) == False:
#             arr_s[i] = -1
#     new_s = ''
#     for i in range(len(arr_s)):
#         if arr_s[i] != -1:
#             new_s += chr(arr_s[i])
#     return new_s

def toArray(str):
    arr = []
    for i in range(len(str)):
        arr.append(ord(str[i]))
    return arr

def check(s, t):
    for i in range(len(s)):
        if (s[i] == t[0]):
            if (len(t) == 1):
                return True
            k = i + 1
            j = 1
            while (k < len(s) and j < len(t) ):
                if (s[k] != t[j]):
                    k += 1 # Changed from break to k += 1 to handle the case when t is in s but not continuous
                    # for example s = "xxxxxxxabcxxxdxe" and t = "abcde"
                if(j == len(t)-1):
                        return True
                k += 1
                j += 1
    return False

if (len(s) < len(t)):
    print('need tree')

# First check if s can be transformed to t
arr_s = toArray(s)
arr_t = toArray(t)
arr_s.sort()
arr_t.sort()
arr_s_for_build = []
i = 0
j = 0
while (i < len(arr_s) and j < len(arr_t)):
    if(arr_s[i] == arr_t[j]):
        arr_s[i] = -1
        arr_t[j] = -1
        arr_s_for_build.append(s[i])
        i += 1
        j += 1
    else:
        i += 1

s_test = []
t_test = []
for i in range(len(arr_s)):
    if arr_s[i] != -1:
        s_test.append(arr_s[i])
for i in range(len(arr_t)):
    if arr_t[i] != -1:
        t_test.append(arr_t[i])


if len(t_test) != 0:
    print('need tree')
else:
    if (len(s_test) != 0):
        # s = processString(s, t)
        if check(s, t) == False:
            print('both')
        else:
            print('automaton')
    else:
        if(check(s, t) == False):
            print('array')
        # else:
        #     print('no need')
