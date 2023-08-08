class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return f'{self.key}'

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


def createTree(a):
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


def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        val = root.key
        print(val, end=' ')
        traversalTree(root.right)

def rotateLeft(root, pivot):
    root.right = minValueNode(root.right)
    pivot.left = root
    root = pivot
    return root


def maxValueNode(root):
    if root.right == None:
        return root
    return maxValueNode(root.right)


def rotateRight(root, pivot):
    root.left = maxValueNode(pivot)
    pivot.right = root
    root = pivot
    return root


a = [5,3,7,2,4,1,6,7,8,9,10, 20, 15, 25, 14, 18, 21, 27]
root = createTree(a)
traversalTree(root)

print()

print(root.left, root.right)

a = 20
root = deleteNode(root, a)
insertNode(root, a)
