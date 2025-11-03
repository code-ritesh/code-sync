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
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        helper(root, res);

        int s = 0;
        int e = res.size()-1;

        while (s <= e) {
            int sum = res.get(s) + res.get(e);

            if (sum == k)
                return true;
            else if (sum < k)
                s++;
            else
                e--;
        }

        return false;

    }

    void helper(TreeNode root, List<Integer> res) {
        if (root == null)
            return;

        helper(root.left, res);
        res.add(root.val);
        helper(root.right, res);
    }
}