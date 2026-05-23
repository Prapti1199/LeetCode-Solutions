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
        if(head == null || n==0){
            return head;
        }
        ListNode fastPnt = head;
        ListNode slowPnt = head;
        int cnt = 0;

        while(cnt < n){
            fastPnt = fastPnt.next;
            cnt ++;
        }
        if(fastPnt == null){
            return head.next;
        }

        while(fastPnt.next != null){
            fastPnt = fastPnt.next;
            slowPnt = slowPnt.next;
        }

        slowPnt.next = slowPnt.next.next;
        return head;
        
    }
}