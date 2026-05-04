class Solution {

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0)
            return null;

        return partitionAndMerge(lists, 0, lists.length - 1);
    }

    private ListNode partitionAndMerge(ListNode[] lists, int start, int end) {
        if (start == end)
            return lists[start];

        if (start > end)
            return null;

        int mid = start + (end - start) / 2;

        ListNode left = partitionAndMerge(lists, start, mid);
        ListNode right = partitionAndMerge(lists, mid + 1, end);

        return mergeTwoLists(left, right);
    }

    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }

        // attach remaining nodes
        if (l1 != null)
            tail.next = l1;
        else
            tail.next = l2;

        return dummy.next;
    }
}