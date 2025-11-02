class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val)
            return root;

        TreeNode ans = null;

        if (val < root.val) {
            //left subtree
            ans = searchBST(root.left, val);
        }

        else
            ans = searchBST(root.right, val);

        return ans;
    }
}