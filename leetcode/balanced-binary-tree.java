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
    public boolean isBalanced(TreeNode root) {
        if(root == null) return true;

        int h = height(root);

        if(h == -1) return false;
        return true;
    }

    int height(TreeNode root){
        if(root == null) return 0;

        int lst = height(root.left);
        int rst = height(root.right);

        if(lst == -1 || rst == -1) return -1;

        if(Math.abs(lst-rst) > 1) return -1;

        return 1 + Math.max(lst,rst);
    }
}