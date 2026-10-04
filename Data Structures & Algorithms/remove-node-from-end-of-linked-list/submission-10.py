# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        count=0
        while ptr:
            count+=1
            ptr=ptr.next
        eliminateindex = count - n #2
        print(eliminateindex)

        ptr=head
        prev=None
        for i in range(eliminateindex):
            prev=ptr
            ptr=ptr.next

        if prev:
            prev.next=ptr.next
            ptr.next=None
        else:
            head=head.next

        

        return head

        