class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        sums = []
        summation = 0
        self.dfs(root, summation, sums)
        return targetSum in sums

    def dfs(self, node, summation, sums):
        if self.isLeaf(node):
            sums.append(summation + node.val)
        if node.left:
            self.dfs(node.left, summation + node.val, sums)
        if node.right:
            self.dfs(node.right, summation + node.val, sums)

    def isLeaf(self, node):
        return not node.left and not node.right
