# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p): #only one exists
            return False
        
        elif p and q and p.val!=q.val: #both exist bit diff val
            return False
        
        elif not p and not q:
            return True
        
        if p and q and p.val==q.val: #both exists same val
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
            
        