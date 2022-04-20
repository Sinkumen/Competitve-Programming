# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder(root)
        self.stack = self.stack[::-1]
        
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        self.stack.append(node.val)
        self.inorder(node.right)
        
        
        
    def next(self) -> int:
        return self.stack.pop()
        

    def hasNext(self) -> bool:
        return True if self.stack else False 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()