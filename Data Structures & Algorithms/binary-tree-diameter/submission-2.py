# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #return a roots longest path from both left and right

        if not root:
            return 0
        count = (self.maxDepth(root.left)+self.maxDepth(root.right))
        count= max(count, self.diameterOfBinaryTree(root.left))
        count= max(count, self.diameterOfBinaryTree(root.right))
        return count


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max( self.maxDepth(root.left),self.maxDepth(root.right) )
