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

class pair {
    TreeNode node;
    int x;
    int y;

    pair(TreeNode node, int x, int y) {
        this.node = node;
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
         List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;

        Queue <pair> q = new LinkedList<>();

        TreeMap <Integer , TreeMap < Integer ,  PriorityQueue<Integer>>> map = new  TreeMap<>();

        q.offer(new pair(root,0,0));

        while(!q.isEmpty()){
            pair p = q.poll();
            int vertical = p.x;
            int level = p.y;
            TreeNode curr = p.node;

            map.putIfAbsent(vertical , new TreeMap<>());
            map.get(vertical).putIfAbsent(level , new PriorityQueue<>());

            map.get(vertical).get(level).offer(curr.val);

            if(curr.left != null){
                q.offer(new pair(curr.left , vertical-1 , level+1));
            }

            if(curr.right != null){
                q.offer(new pair(curr.right , vertical+1 , level+1));
            }
        }


        for( var  temp : map.values() ){
            ArrayList<Integer> curr = new ArrayList<>();

            for( var pq : temp.values()){
                while(!pq.isEmpty()){
                    curr.add(pq.poll());
                }
            }

            res.add(curr);
        }

        return res;
    }
}