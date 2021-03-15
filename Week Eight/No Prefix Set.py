class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word:
            if current.end:
                return False
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]

        if current.end or bool(current.children):
            return False
        current.end = True
        return True


class Node:
    def __init__(self):
        self.children = {}
        self.end = False


def noPrefix(words):
    # Write your code here
    trie = Trie()
    for word in words:
        inserted = trie.insert(word)
        if not inserted:
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
    return
