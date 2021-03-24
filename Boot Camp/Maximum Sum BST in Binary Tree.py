# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root) -> int:
        def dfs(node):
            if isLeaf(node):
                return (node.val, node.val, node.val, node.val, node.val)

            if node.left and node.right:
                left = dfs(node.left)
                right = dfs(node.right)

                # checking
                # 1) if the  current node is greater than left node and smaller than right node in order to be BST
                # 2) if the current sum of valid bst from left and right is None Or not if not none we add ourselves to it
                # 3) if the upper bound and lower bound of the sub tree to check for BST Validation
                if left[0] < node.val < right[0] and (left[2] != None and right[2] != None and right[3] > node.val and left[4] < node.val):
                    curr = left[2] + right[2] + node.val
                    glob = max(curr, left[1], right[1])
                    curmin = min(left[3], right[3], node.val)
                    curmax = max(left[4], right[4], node.val)
                    return (node.val, glob, curr, curmin, curmax)
                else:
                    glob = max(left[1], right[1])
                    return (node.val, glob, None, 0, 0)

            elif node.left:
                left = dfs(node.left)
                if left[0] < node.val and left[2] != None and left[4] < node.val:
                    curr = left[2] + node.val
                    glob = max(curr, left[1])
                    curmin = min(left[3], node.val)
                    curmax = max(left[4], node.val)
                    return (node.val, glob, curr, curmin, curmax)
                else:
                    return (node.val, left[1], None, 0, 0)
            elif node.right:
                right = dfs(node.right)
                if right[0] > node.val and right[2] != None and right[3] > node.val:
                    curr = right[2] + node.val
                    glob = max(curr, right[1])
                    curmin = min(right[3], node.val)
                    curmax = max(right[4], node.val)
                    return (node.val, glob, curr, curmin, curmax)
                else:
                    return (node.val, right[1], None, 0, 0)

        def isLeaf(node):
            return not node.left and not node.right
        if isLeaf(root):
            return root.val
        return max(dfs(root)[1], 0)
