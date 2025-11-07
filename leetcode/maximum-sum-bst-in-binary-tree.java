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
    int ans;

    public int maxSumBST(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }

    //// Returns an array of size 3 -> {minValue, maxValue, sumOfSubtree}
    public int[] dfs(TreeNode root) {

        if (root == null)
            return new int[] { Integer.MAX_VALUE, Integer.MIN_VALUE, 0 };

        int[] leftST = dfs(root.left);
        int[] rightST = dfs(root.right);

        if (root.val > leftST[1] && root.val < rightST[0]) {
            int curSum = leftST[2] + rightST[2] + root.val;
            ans = Math.max(ans, curSum);
            int minVal = Math.min(root.val, leftST[0]);
            int maxVal = Math.max(root.val, rightST[1]);
            return new int[] { minVal, maxVal, curSum };
        }

        int maxSum = Math.max(leftST[2], rightST[2]);
        return new int[] { Integer.MIN_VALUE, Integer.MAX_VALUE, maxSum };
    }
}