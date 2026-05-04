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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode a = list1;
        ListNode b = list2;

        ListNode ans = new ListNode(-1);
        ListNode curr = ans;

        while(a != null && b != null ){
            if(a.val <= b.val ){
                curr.next = a;
                a = a.next;
            }

            else{
                curr.next = b;
                b = b.next;
            }

            curr = curr.next;
        }

        while(a != null ){
            curr.next = a;
            a = a.next;
            curr = curr.next;
        }

        while(b != null ){
            curr.next = b;
            b = b.next;
            curr = curr.next;
        }

        return ans.next;
    }
}