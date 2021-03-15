class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not current.children[index]:
                current.children[index] = Node(char)
            current = current.children[index]
        current.isEnd = True

    def search(self, word):
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current.children[index]:
                current = current.children[index]
            return False
        return True if current.isEnd else False

    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if current.children[index]:
                current = current.children[index]
            else:
                return False
        return True

    def printNodes(self, node=None):
        current = self.root if not node else node
        res = []
        for node in current.children:
            if node:
                res.append(node.value)
                self.printNodes(node)
        print(current.value, res)


class Node:
    def __init__(self, char=None):
        self.value = char
        self.children = [None]*26
        self.isEnd = False


tr = Trie()
tr.insert("word")
tr.insert("work")
tr.printNodes()
print(tr.search("wor"))
