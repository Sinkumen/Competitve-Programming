class Node:
    def __init__(self):
        self.children = {}
        self.words = []
        self.isEnd = False
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node()
        products.sort()
        for word in products:
            cur  = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node()
                cur = cur.children[char]
                cur.words.append(word)
            cur.isEnd = True
        ans = []
        cur = root
        correct = True
        for char in searchWord:
            if char in cur.children and correct:
                cur = cur.children[char]
                ans.append(cur.words[:3])
            else:
                correct = False
                ans.append([])
        return ans
            
            