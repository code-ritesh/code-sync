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
    public boolean isSymmetric(TreeNode root) {
        if(root == null ) return true;

        return mirror(root.left,root.right);
    }

    boolean mirror(TreeNode lefty , TreeNode righty){
        if(lefty == null || righty == null ) return lefty == righty;

        if(lefty.val != righty.val ) return false;

        return mirror(lefty.left , righty.right) && mirror(lefty.right , righty.left);
    }
}