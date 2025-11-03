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

    int pos = 0;

    public int kthSmallest(TreeNode root, int k) {

        TreeNode ans = helper(root, k);

        if (ans == null)
            return -1;

        return ans.val;
    }

    TreeNode helper(TreeNode root, int k) {
        if (root == null)
            return root;

        TreeNode left = helper(root.left, k);

        if (left != null)
            return left;

        pos++;

        if (k == pos)
            return root;

        TreeNode right = helper(root.right, k);

        if (right != null)
            return right;

        return null;
    }
}