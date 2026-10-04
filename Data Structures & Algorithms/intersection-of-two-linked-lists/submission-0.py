# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA= headA
        ptrB=headB
        countA=0
        countB=0
        while ptrA:
            countA+=1
            ptrA=ptrA.next
        while ptrB:
            countB+=1
            ptrB=ptrB.next
        ptrA=headA
        ptrB=headB
        if countA>countB:
            for i in range(countA-countB):
                if ptrA.next:
                    ptrA=ptrA.next
        else:            
            for i in range(countB-countA):
                if ptrB.next:
                    ptrB=ptrB.next

        while ptrA and ptrB:
            if ptrA==ptrB:
                return ptrA
            ptrA=ptrA.next
            ptrB=ptrB.next

        return None
