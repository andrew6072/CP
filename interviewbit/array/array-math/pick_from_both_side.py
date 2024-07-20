def solve(A, B):
    left = B - 1
    right = len(A) - 1
    s = sum(A[:B])
    a = s
    while left >= 0:
        s -= A[left]
        s += A[right]
        a = max(a, s)
        left -= 1
        right -= 1
    return a
