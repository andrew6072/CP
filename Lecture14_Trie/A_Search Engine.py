class TrieNode:
    def __init__(self):
        self.child = dict()
        self.isEndOfWord = False

    def __repr__(self):
        char_in_dict = []
        for i in range(97, 123):
            if chr(i) in self.child:
                char_in_dict.append(chr(i))
        return "Children -> " + str(char_in_dict)


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = TrieNode()
        temp = temp.child[ch]
    temp.isEndOfWord = True
