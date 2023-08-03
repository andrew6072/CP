class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def createNode(x):
    return Node(x)


def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x < root.key:
        root.left = insertNode(root.left, x)
    elif x > root.key:
        root.right = insertNode(root.right, x)
    return root


def createTree(a, n):
    root = None
    for x in a:
        root = insertNode(root, x)
    return root



n = int(input())
a = list(map(int, input().split()))
min_diff = 10**17
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            min_diff = min(a[i]-a[j], min_diff)
print(min_diff)
