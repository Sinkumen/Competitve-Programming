# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxProd = [0]

    def maxProduct(self, root) -> int:

        totalSum = self.sumTree(root)
        self.dfs(root, totalSum)
        return self.maxProd[0] % (10**9+7)

    def dfs(self, node, totalSum):
        if self.isLeaf(node):
            subTreeSum = node.val
            self.maxProd[0] = max(
                self.maxProd[0], (totalSum-subTreeSum)*subTreeSum)
            return node.val

        if node.left and node.right:
            left = self.dfs(node.left, totalSum)
            right = self.dfs(node.right, totalSum)
            subTreeSum = (left + right + node.val)
            self.maxProd[0] = max(
                self.maxProd[0], (totalSum-subTreeSum)*subTreeSum)
            return subTreeSum
        elif node.left:
            left = self.dfs(node.left, totalSum)
            subTreeSum = (left + node.val)
            self.maxProd[0] = max(
                self.maxProd[0], (totalSum-subTreeSum)*subTreeSum)
            return subTreeSum
        elif node.right:
            right = self.dfs(node.right, totalSum)
            subTreeSum = (right + node.val)
            self.maxProd[0] = max(
                self.maxProd[0], (totalSum-subTreeSum)*subTreeSum)
            return subTreeSum

    def sumTree(self, node):
        if self.isLeaf(node):
            return node.val
        summ = node.val
        if node.left:
            summ += self.sumTree(node.left)
        if node.right:
            summ += self.sumTree(node.right)
        return summ

    def isLeaf(self, node):
        return not node.left and not node.right
