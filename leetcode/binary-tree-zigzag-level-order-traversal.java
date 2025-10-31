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

    

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null)
            return result;

        Queue<TreeNode> q = new LinkedList<>();

        q.offer(root);

        boolean rev = false;

        while (!q.isEmpty()) {
            int size = q.size();

            List<Integer> sub = new ArrayList<>();

            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();

                sub.add(curr.val);

                if(curr.left != null) q.offer(curr.left);
                if(curr.right != null) q.offer(curr.right);

            }

            if(rev){
                Collections.reverse(sub);
            }

            result.add(new ArrayList<>(sub));

            rev = !rev;

        }

        return result;
    }
}