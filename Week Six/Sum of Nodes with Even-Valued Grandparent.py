class Solution:
    def __init__(self):
        self.sum = 0

    def sumEvenGrandparent(self, root) -> int:
        if not root:
            return 0
        self.dfs(root, None, None)
        return self.sum

    def dfs(self, c, p, gb):
        if gb and gb.val % 2 == 0:
            self.sum += c.val
        if c.left:
            self.dfs(c.left, c, p)
        if c.right:
            self.dfs(c.right, c, p)
