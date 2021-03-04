class Solution:
    def longestUnivaluePath(self, root) -> int:
        return self.helper(root)[0]

    def helper(self, root):
        left = (0, 0)
        right = (0, 0)

        result = (0, 0)

        leftCompatible = False
        rightCompatible = False

        if not root or (not root.left and not root.right):
            return (0, 0)

        if root.left:
            leftCompatible = root.val == root.left.val
            left = self.helper(root.left)

        if root.right:
            rightCompatible = root.val == root.right.val
            right = self.helper(root.right)

        if leftCompatible:
            result = (result[0], left[1] + 1)
        if rightCompatible and right[1] + 1 > result[1]:
            result = (result[0], right[1] + 1)

        result = (max(right[0], left[0]), result[1])
        localBest = 0

        if leftCompatible and rightCompatible:
            localBest = left[1] + right[1] + 2
        elif(leftCompatible):
            localBest = left[1] + 1
        elif(rightCompatible):
            localBest = right[1] + 1

        if(localBest > result[0]):
            result = (localBest, result[1])

        return result
