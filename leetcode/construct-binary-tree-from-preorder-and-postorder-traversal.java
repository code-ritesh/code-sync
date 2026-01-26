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
    int preidx = 0;
    Map <Integer , Integer> map = new HashMap<>();

    TreeNode helper(int[] preorder, int[] postorder , int poststart , int postend){
        if(poststart > postend ) return null;

        int rootval = preorder[preidx++];
        TreeNode root = new TreeNode(rootval);

        if(poststart == postend ) return root;

        int leftchild = preorder[preidx];
        int leftchildidx = map.get(leftchild);

        root.left = helper(preorder,postorder,poststart,leftchildidx);
        root.right = helper(preorder,postorder,leftchildidx+1,postend-1);

        return root;
    }

    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        int n = preorder.length;

        for(int i = 0 ; i < n ; i++){
            map.put(postorder[i] , i);
        }

        return helper(preorder,postorder,0,n-1);
    }
}