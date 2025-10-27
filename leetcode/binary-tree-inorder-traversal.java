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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();
        TreeNode node = root;

        while (node != null || !st.isEmpty()) {
            // go as far left as possible
            while (node != null) {
                st.push(node);
                node = node.left;
            }

            // pop from stack (visit node)
            node = st.pop();
            ans.add(node.val);

            // move to right child
            node = node.right;
        }

        return ans;
    }
}