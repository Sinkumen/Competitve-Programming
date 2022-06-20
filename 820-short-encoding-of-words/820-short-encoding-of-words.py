class Node:
    def __init__(self,isRoot=False):
        self.children = {}
        self.isEnd = 0
        self.isRoot = isRoot
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Node(True)
        ans = 0
        for word in words:
            cur = root
            for char in word[::-1]:
                if char not in cur.children:
                    cur.children[char] = Node()
                cur = cur.children[char]
            cur.isEnd += 1
        
        def dfs(node):
            res = 0
            count = 0
            for nxt in node.children:
                temp = dfs(node.children[nxt])
                res += temp[0]
                count += temp[1]
        
            if not res and node.isEnd:
                return (2,1)
            
            if node.isRoot:
                return res
            
            return (res + count,count)
                
        return dfs(root)
            