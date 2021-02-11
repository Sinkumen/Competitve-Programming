class Solution:
    def findBottomLeftValue(self, root) -> int:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return (0, 0)

        if not root.left and not root.right:
            return (root.val, 1)

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left[1] < right[1]:
            return (right[0], right[1]+1)
        else:
            return (left[0], left[1]+1)
