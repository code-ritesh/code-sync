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

// Go as far left as possible and push nodes on a stack.

// When you can’t go left anymore:

// If the top of the stack has an unvisited right child, move right.

// Otherwise, process (visit) the node (add its value to result).

// Continue until both left and right subtrees are processed.


class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();

        TreeNode node = root;

        while (node != null || !st.isEmpty()) {
            // move left
            while (node != null) {
                st.push(node);
                node = node.left;
            }

            // move right

            if (st.peek().right != null) {
                node = st.peek().right;
            } else {
                TreeNode temp = st.pop();
                res.add(temp.val);

                while (!st.isEmpty() && temp == st.peek().right) {
                    temp = st.pop();
                    res.add(temp.val);
                }
            }
        }

        return res;
    }
}