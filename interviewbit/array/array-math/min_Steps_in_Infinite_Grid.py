# A = [4, 1, 4, 10]
# B = [6, 2, 5, 12]
A = [0, 1, 0]
B = [0, 1, 0]


def solve(A, B):
    if A[0] == A[-1] and B[0] == B[-1]:
        return 0
    COUNT = 0
    for i in range(1, len(A)):
        COUNT += max(A[i] - A[i-1], B[i] - B[i-1])
    return COUNT
