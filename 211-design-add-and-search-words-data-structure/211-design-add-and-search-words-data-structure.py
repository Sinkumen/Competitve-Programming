class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = Node()        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(i,cur):
            if i >= len(word):
                if cur.isEnd:
                    return True
                return False
            if word[i] == ".":
                for nxt in cur.children.keys():
                    res = dfs(i+1,cur.children[nxt])
                    if res: return True
                return False
            elif word[i] in cur.children:
                return dfs(i+1,cur.children[word[i]])
            else:
                return False
        return dfs(0,self.root)
                
     
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)