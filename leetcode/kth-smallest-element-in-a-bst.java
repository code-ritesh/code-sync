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
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        helper(root, res);

        for(int i = 0 ; i < res.size() ; i++){
            if(i + 1 == k ) return res.get(i);
        }

        return -1;
    }

    void helper(TreeNode root, List<Integer> res) {
        if (root == null)
            return;

        helper(root.left, res);
        res.add(root.val);
        helper(root.right, res);
    }
}