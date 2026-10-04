# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = list1
        ptr2 = list2
        
        newnode=ListNode(0)
        ptr=newnode

        while ptr1 and ptr2:
            
            if (ptr1.val > ptr2.val): #second one is smaller
                ptr.next = ptr2
                ptr2=ptr2.next
            else:
                ptr.next=ptr1
                ptr1=ptr1.next
            ptr=ptr.next

        while ptr1:
            # print("got in here")
            ptr.next=ptr1
            ptr1=ptr1.next
            ptr=ptr.next
        while ptr2:
            ptr.next=ptr2
            ptr2=ptr2.next
            ptr=ptr.next
            
        return newnode.next
        
        