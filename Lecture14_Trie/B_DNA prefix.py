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


def printWord(root, s):
    if root.isEndOfWord:
        print(s)
    for ch in root.child:
        content = str(root.child[ch])
        printWord(root.child[ch], s + content)


# debug this to see what if we don't have res in for loop
def findMaxRes(root, res):
    res = max(res, root.num_words * root.depth)
    for ch in root.child:
        res = findMaxRes(root.child[ch], res)
    return res


root = TrieNode()
addWord(root, 'ACGT')
addWord(root, 'ACGTGCGT')
addWord(root, 'ACCGTGC')
addWord(root, 'ACGCCGT')

res = findMaxRes(root, -1)
print(res)

# tc = int(input())
# for i in range(tc):
#     n = int(input())
#
#     root = TrieNode()
#     for _ in range(n):
#         content = input()
#         addWord(root, content)
#
#     res = -1
#     res = findMaxRes(root, res)
#     print(f'Case {i+1}: {res}')
