# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])

        result=[]
        rightside=[]
        while queue:
            rightside.append(queue[-1].val)

            for _ in range(len(queue)):
                node=queue.popleft()
                value=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside
        # queue=[1]
        # queue=[2,3]
        # queue=[3,4,5]
        #

            
