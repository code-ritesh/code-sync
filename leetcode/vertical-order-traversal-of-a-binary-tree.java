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

class Pair {
    TreeNode node;
    int x;
    int y;

    public Pair(int _x, int _y, TreeNode _node) {
        x = _x;
        y = _y;
        node = _node;
    }
}

class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        //your code goes here
        List<List<Integer>> result = new ArrayList<>();
        if (root == null)
            return result;
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();
        Queue<Pair> queue = new LinkedList<>();

        queue.offer(new Pair(0, 0, root));

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int x = pair.x;
            int y = pair.y;
            TreeNode node = pair.node;

            map.putIfAbsent(x, new TreeMap<>());
            map.get(x).putIfAbsent(y, new PriorityQueue<>());

            map.get(x).get(y).offer(node.val);

            if (node.left != null) {
                queue.offer(new Pair(x - 1, y + 1, node.left));
            }
            if (node.right != null) {
                queue.offer(new Pair(x + 1, y + 1, node.right));
            }
        }
        
        for (var val : map.values()) {
            List<Integer> curr = new ArrayList<>();
            for (var v : val.values()) {
                while (!v.isEmpty()) {
                    curr.add(v.poll());
                }
            }
            result.add(curr);
        }
        return result;
    }
}