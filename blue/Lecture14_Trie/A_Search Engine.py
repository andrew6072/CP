class TrieNode:
    def __init__(self, priority):
        self.child = dict()
        self.priority = priority
        self.isEndOfWord = False

    def __repr__(self):
        char_in_dict = []
        for i in range(97, 123):
            if chr(i) in self.child:
                char_in_dict.append(chr(i))
        return '(' + str(self.priority) + ', ' + str(self.child) + ')'

    def setPriority(self, priority):
        self.priority = priority


def addWord(root, s, priority):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = TrieNode(priority)
        elif priority > temp.child[ch].priority:
            temp.child[ch].setPriority(priority)
        temp = temp.child[ch]
    temp.isEndOfWord = True

def printTrie(root, s):
    if root.isEndOfWord == True:
        print(s, root.priority)
    for ch in root.child.keys():
        printTrie(root.child[ch], s + ch)


def getMaxPriority(root, s):
    temp = root
    for char in s:
        if char not in temp.child:
            return -1
        temp = temp.child[char]
    return temp.priority


n, q = map(int, input().split())
root = TrieNode(0)
for _ in range(n):
    str, p = input().split()
    addWord(root, str, int(p))
for _ in range(q):
    key = input()
    print(getMaxPriority(root, key))
