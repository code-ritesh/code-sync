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

    HashMap<Integer, Integer> map;
    int idx = 0;

    TreeNode helper(int[] preorder, int[] inorder, int start, int end) {
        if(start > end) return null;

        int rootval = preorder[idx];
        idx++;

        TreeNode root = new TreeNode(rootval);

        // find index in inorder

        int inorderidx = map.get(rootval);

        root.left = helper(preorder,inorder,start,inorderidx-1);
        root.right = helper(preorder,inorder,inorderidx+1,end);

        return root;

    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        map = new HashMap<>();
        int n = inorder.length;

        for (int i = 0; i < n; i++) {
            map.put(inorder[i], i);
        }

        return helper(preorder , inorder , 0 , n-1 );

    }
}