# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        curr1 = l1
        curr2 = l2
        carry = 0
        root=ListNode(0)
        ptr=root


        while curr1 or curr2:
            if(not curr1):
                value1 = 0
            else:
                value1 = curr1.val
            if (not curr2):
                value2 = 0 
            else:
                value2= curr2.val

            sumofdigit = value1+value2+carry #calcualte sum of digit
            print(sumofdigit)
            carry=0
            if(sumofdigit >= 10):
                carry = 1
            newnode = ListNode(sumofdigit%10)
            ptr.next=newnode
            if(curr1):    
                curr1=curr1.next
            if(curr2):
                curr2=curr2.next
            ptr=ptr.next

        if (carry ==1):
            newnode = ListNode(1)
            ptr.next=newnode
        


        return root.next

            

