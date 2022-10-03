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
    public ListNode mergeKLists(ListNode[] lists) {
         PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b) -> a.val-b.val);
        for(ListNode list:lists)
        {
            if(list!=null)
            {
                pq.add(list);
            }
            
        }
        ListNode head=null;
        ListNode tail=null;
        
        while(!pq.isEmpty())
        {
            ListNode current=pq.poll();
            if(head==null)
            {
                head=current;
                tail=current;
                
            }
            else
            {
                tail.next=current;
                tail=current;
                
            }
            if(current.next!=null)
                pq.add(current.next);
        }
        return head;
}
}