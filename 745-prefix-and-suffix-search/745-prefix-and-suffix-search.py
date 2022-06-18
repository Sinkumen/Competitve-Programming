class Node:
    def __init__(self):
        self.children = {}
        self.indices = []
        self.isEnd = False
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = Node()
        
        for i in range(len(words)):
            for j in range(len(words[i])-1,-1,-1):
                query = f"{words[i][j:]}#{words[i]}"
                cur = self.root
                for char in query:
                    if char not in cur.children:
                        cur.children[char] = Node()
                    cur = cur.children[char]
                    cur.indices.append(i)
                cur.isEnd = True
        
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.root
        query = suffix+"#"+prefix
        # print(query)
        found = True
        for char in query:
            if char not in cur.children:
                found = False
                break
            prev = cur
            cur = cur.children[char]
        # print(cur.indices)
        if found:
            return cur.indices[-1]
        return -1
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)