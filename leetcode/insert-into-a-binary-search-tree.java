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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            root = new TreeNode(val);
            return root;
        }

        // left < root < right -> condition for bst 

        TreeNode temp = root;

        while (temp != null) {
            //left subtree
            if (val < temp.val ) {
                if (temp.left == null) {
                    temp.left = new TreeNode(val);
                    break;
                }

                else
                    temp = temp.left;
            }

            // right subtree
            else {
                if (temp.right == null) {
                    temp.right = new TreeNode(val);
                    break;
                }

                else
                    temp = temp.right;
            }
        }

        return root;
    }
}