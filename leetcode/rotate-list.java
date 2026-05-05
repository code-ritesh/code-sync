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

    public ListNode rotateRight(ListNode head, int k) {

        if (head == null || head.next == null || k == 0)
            return head;

        int ans = 1;
        ListNode temp = head;

        while (temp.next != null) {
            ans++;
            temp = temp.next;
        }

        temp.next = head;

        k = k % ans;

        ListNode lastnode = head;

        for (int i = 1 ; i < ans - k  ; i++) {
            lastnode = lastnode.next;
        }

        ListNode newhead = lastnode.next;
        lastnode.next = null;

        return newhead;

    }
}