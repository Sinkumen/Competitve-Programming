class Solution:
    def isValidBST(self, root) -> bool:
        upper = 2**31
        lower = -2**31-1
        return self.helper(root, upper, lower)

    def helper(self, root, upper, lower):
        if not root:
            return True
        if root.left and (root.val <= root.left.val) or root.right and (root.val >= root.right.val):
            return False
        if(root.val >= upper) or (root.val <= lower):
            return False
        return self.helper(root.right, upper, root.val) and self.helper(root.left, root.val, lower)
