/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode ptr = head;
        int count = 1;
        if(head.next==null && n==1) return null;
        while(ptr.next!=null){
            count++;
            ptr=ptr.next;
        }

        int fromstartnth=count-n;
        ListNode ptr1 = head;

        if(fromstartnth == 0){
            head=head.next;
            
        }
        else{
            for(int i = 1; i<fromstartnth;i++){
                ptr1=ptr1.next;
            }
            ptr1.next=ptr1.next.next;
        }



        return head;


    }
}
