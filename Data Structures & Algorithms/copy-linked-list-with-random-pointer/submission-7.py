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
        d={}
        while ptr:
            newnode = Node(ptr.val)
            d[ptr]=newnode
            ptr=ptr.next
        
        for i in d:
            #d[i] newnode and i is the original node
            if(i.next):
                d[i].next = d[i.next]
            else:
                d[i].next=None
            if i.random:
                d[i].random = d[i.random]
            else:
                d[i].random=None
        return d[head]