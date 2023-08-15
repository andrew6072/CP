class TrieNode:
    def __init__(self, content='', num_words=0, depth=0):
        self.content = content
        self.child = dict()
        self.isEndOfWord = False
        self.num_words = num_words
        self.depth = depth

    def __repr__(self):
        return f'(ch: {self.content}, n: {self.num_words}, d: {self.depth})'

    def __str__(self):
        return f'(ch: {self.content}, n: {self.num_words}, d: {self.depth})'


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = TrieNode(ch,1, temp.depth + 1)
        else:
            temp.child[ch].num_words += 1
        temp = temp.child[ch]
    temp.isEndOfWord = True


def findMaxRes(root, res):
    res = max(res, root.num_words)
    for ch in root.child:
        res = findMaxRes(root.child[ch], res)
    return res


def printWord(root, s):
    if root.isEndOfWord:
        print(s)
    for ch in root.child:
        content = str(root.child[ch])
        printWord(root.child[ch], s + content)


def hasPrefix(root):
    if root.isEndOfWord and len(root.child) > 0:
        return True

    for ch in root.child:
        if hasPrefix(root.child[ch]):
            return True

    return False



def solve():
    n = int(input())
    root = TrieNode()
    for _ in range(n):
        number = input()
        addWord(root, number)
    return hasPrefix(root)

tc = int(input())
for _ in range(tc):
    ans  = solve()
    if ans:
        print('NO')
    else:
        print('YES')