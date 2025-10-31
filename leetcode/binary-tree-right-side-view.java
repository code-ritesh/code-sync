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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while(!q.isEmpty()){
            int size = q.size();

            // use for loop instead of while(size > 0)
            for(int i = 0; i < size; i++){
                TreeNode curr = q.poll();

                // add children to queue
                if(curr.left != null) q.offer(curr.left);
                if(curr.right != null) q.offer(curr.right);

                // last node in the level is the rightmost
                if(i == size - 1) res.add(curr.val);
            }
        }

        return res;
    }
}