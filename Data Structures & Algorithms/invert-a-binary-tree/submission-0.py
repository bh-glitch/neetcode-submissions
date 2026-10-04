# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        result=[]
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(node)
                if node.left and node.right:
                    node.left,node.right=node.right,node.left
                elif node.left and not node.right:
                    node.right=node.left
                    node.left=None
                else:
                    node.left=node.right
                    node.right=None

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result[0]
        # queue = deque([root])
        # result=[]
        # while queue:

        #     for _ in range(len(queue)):
        #         node = queue.pop()
        #         result.append(node)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
                
        # return result[0]

            