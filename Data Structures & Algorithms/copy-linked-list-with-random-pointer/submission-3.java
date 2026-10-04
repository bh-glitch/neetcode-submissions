/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {

        if(head==null) return null;
        Node ptr = head;


        while(ptr!=null){
            Node insert = new Node(ptr.val);
            insert.next=ptr.next;
            ptr.next=insert;

            ptr=ptr.next.next;
        }

        Node mainptr = head;
        while(mainptr!=null){
            if(mainptr.random==null){
                mainptr.next.random=null;
            }
            else{
                mainptr.next.random=mainptr.random.next;

            }
            mainptr=mainptr.next.next;
        }

        Node org = head;
        Node copyHead = head.next;
        Node copy = copyHead;

        while(org!=null && copy!=null){
            org.next=org.next.next;
            if(copy.next==null){
                copy.next=null;
            }
            else{
                copy.next=copy.next.next;
            }
            org=org.next;
            copy=copy.next;
        }
        return copyHead;

    }
}
