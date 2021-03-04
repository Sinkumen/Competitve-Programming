class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self, node):
        if self.isLeaf(node):
            return 1
        if node.left and node.right:
            left = self.dfs(node.left)
            right = self.dfs(node.right)
            return min(left, right) + 1
        if node.left:
            return self.dfs(node.left) + 1
        if node.right:
            return self.dfs(node.right) + 1

    def isLeaf(self, node):
        return not node.left and not node.right
