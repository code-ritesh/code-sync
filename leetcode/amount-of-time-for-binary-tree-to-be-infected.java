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

    HashMap <TreeNode , TreeNode > map = new HashMap<>();

    public int amountOfTime(TreeNode root, int start) {

        if(root == null ) return -1;

        TreeNode startNode = parentmapping(root,start);

        return ans(startNode);
    }

    TreeNode parentmapping(TreeNode root , int start){
        Queue <TreeNode> q = new LinkedList<>();
        q.add(root);
        TreeNode startNode = null;


        while(!q.isEmpty()){
            TreeNode curr = q.poll();

            if(curr.val == start){
                startNode = curr;
            }

            if(curr.left != null ){
                map.put(curr.left , curr);
                q.add(curr.left);
            }

            if(curr.right != null){
                map.put(curr.right,curr);
                q.add(curr.right);
            }
        }

        return startNode;
    }

    int ans(TreeNode startNode){
        int time = -1;
        HashSet<TreeNode> set = new HashSet<>();
        Queue <TreeNode> q = new LinkedList<>();

        q.add(startNode);
        set.add(startNode);

        while(!q.isEmpty()){
            int size = q.size();
            time++;

            for(int i = 0 ; i < size ; i++){

                TreeNode curr = q.poll();

                if(curr.left != null && !set.contains(curr.left)){
                    q.add(curr.left);
                    set.add(curr.left);
                }

                if(curr.right != null && !set.contains(curr.right) ){
                    q.add(curr.right);
                    set.add(curr.right);
                }

                if( map.containsKey(curr) && !set.contains(map.get(curr))){
                    q.add(map.get(curr));
                    set.add(map.get(curr));
                }
            }
        }

        return time;
    }
}