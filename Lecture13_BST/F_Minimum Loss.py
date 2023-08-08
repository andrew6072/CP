class Node:
    def __init__(self, key=-1):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
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


def createTree(a):  # O(N*h) h=log(N) in best case
    root = None
    for x in a:
        root = insertNode(root, x)
    return root


# Function finds min value from tree that is bigger than x
def upperBound(root, x):
    if root == None:
        return root
    if root.key <= x:
        return upperBound(root.right, x)
    elif root.key > x:
        ub_left = upperBound(root.left, x)
        return root if ub_left is None else ub_left


n = int(input())
prices = list(map(int, input().split()))
minimum_loss = 10**17
root = None
for price in prices:
    best_buy = upperBound(root, price)
    if best_buy is not None:
        minimum_loss = min(minimum_loss, best_buy.key - price)
    root = insertNode(root, price)

print(minimum_loss)