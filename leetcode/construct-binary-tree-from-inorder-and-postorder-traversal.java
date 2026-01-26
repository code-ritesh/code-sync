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
    int idx ;
    HashMap<Integer, Integer> map = new HashMap<>();

    TreeNode helper(int[] inorder, int[] postorder, int start, int end) {
        if (start > end)
            return null;

        int rootval = postorder[idx];
        idx--;

        TreeNode root = new TreeNode(rootval);
        int inorderidx = map.get(rootval);

        root.right = helper(inorder, postorder, inorderidx + 1, end);
        root.left = helper(inorder, postorder, start, inorderidx - 1);

        return root;
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int n = inorder.length;
        idx = n-1;

        for (int i = 0; i < n; i++) {
            map.put(inorder[i], i);
        }

        return helper(inorder, postorder, 0, n - 1);
    }
}