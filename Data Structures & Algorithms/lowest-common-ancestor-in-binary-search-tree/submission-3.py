# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val<p.val and root.val<q.val:#to th right
                root = root.right

            elif root.val>p.val and root.val>q.val: # to the left
                root=root.left
            else:
                return root
        



    
