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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        helper(root, targetSum, current, result);

        return result;
    }

    void helper(TreeNode root, int targetSum, List<Integer> current, List<List<Integer>> result) {

        if(root == null ) return ;

        int remaining = targetSum - root.val;
        current.add(root.val);


        // leaf logic
        if(root.left == null &&  root.right == null){
            if(root.val == targetSum){
                result.add(new ArrayList<>(current) );
                                                            }
        }


        helper(root.left , remaining , current , result);
        helper(root.right, remaining , current , result);

        //pop back
        current.remove(current.size() - 1);
    }

}