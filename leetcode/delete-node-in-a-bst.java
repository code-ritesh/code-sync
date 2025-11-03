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
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null ) return root;

        if( key < root.val ){
            // left subtree
            root.left = deleteNode(root.left , key);
        }

        else if( root.val < key ){
            // right subtree
            root.right = deleteNode(root.right , key);
        }

        else{
            // find the answer

            //leaf node case
            if(root.left == null && root.right == null) return null;

            // one node attach case
            if(root.left == null ){
                return root.right;
            }
            else if(root.right == null){
                return root.left;
            }

            else{
                // 2 node attach case
                // predeccsor = left subtree ki max value jo hamesa right pe milege
                // successor = right subtree ki min value jo hamesha left me milegi
                // bcz in bst left < root < right

                // find the precidsor or successor
                TreeNode node = findPredeccesor(root.left);
                // shift the node
                root.val = node.val;
                // delete the node
                root.left = root.left = deleteNode(root.left , node.val);

            }
        }

        return root;
    }

    TreeNode findPredeccesor(TreeNode node){
        while(node.right != null){
            node = node.right;
        }

        return node;
    }
}