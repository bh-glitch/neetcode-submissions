"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (not head):
            return None
        ptr=head
        d={None:None}
        while ptr:
            newnode = Node(ptr.val)
            d[ptr]=newnode
            ptr=ptr.next
        ptr=head
        
        while ptr:
            #d[i] newnode and i is the original node
            d[ptr].next = d[ptr.next]
            d[ptr].random = d[ptr.random]
            ptr=ptr.next

        return d[head]