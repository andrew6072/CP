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


def searchNode(root, x):
    if root == None or root.key == x:
        return root
    if x > root.key:
        return searchNode(root.right, x)
    return searchNode(root.left, x)


def deleteNode(root, x):
    if root == None:
        return root
    if x < root.key:
        root.left = deleteNode(root.left, x)
    elif x > root.key:
        root.right = deleteNode(root.right, x)
    else: # when x == root.key
        if root.left == None:
            temp = root.right
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


def minValueNode(root):
    if root.left == None:
        return root
    return minValueNode(root.left)


n = int(input())
a = list(map(int, input().split()))
min_diff = 10**17
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            min_diff = min(a[i]-a[j], min_diff)
print(min_diff)
