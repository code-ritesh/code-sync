/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode> q = new LinkedList<>();

        if (root == null)
            return false;

        int child = 0;

        q.offer(root);

        while (!q.isEmpty()) {
            int n = q.size();

            for (int i = 0; i < n; i++) {
                TreeNode curr = q.poll();
                int parent = 0;

                if (curr.left != null) {

                    if (curr.left.val == x || curr.left.val == y) {
                        parent++;
                        child++;
                    }
                    q.offer(curr.left);
                }

                if (curr.right != null) {
                    if (curr.right.val == x || curr.right.val == y) {
                        parent++;
                        child++;
                    }
                    q.offer(curr.right);
                }

                if (parent == 2)
                    return false;
            }

            if (child == 2)
                return true;
            if (child == 1)
                return false;

        }

        return false;
    }
}