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
    int x; // column index
    int y; // level index

    Pair(TreeNode node, int x, int y) {
        this.node = node;
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;

        Queue<Pair> q = new LinkedList<>();

        // TreeMap structure:
        // x → TreeMap<y, PriorityQueue<Integer>>
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();

        q.offer(new Pair(root, 0, 0));

        while (!q.isEmpty()) {
            Pair p = q.poll();
            int vertical = p.x; // column
            int level = p.y; // depth/row
            TreeNode curr = p.node;

            map.putIfAbsent(vertical, new TreeMap<>());
            map.get(vertical).putIfAbsent(level, new PriorityQueue<>());
            map.get(vertical).get(level).offer(curr.val);

            // Add left child
            if (curr.left != null) {
                q.offer(new Pair(curr.left, vertical - 1, level + 1));
            }

            // Add right child
            if (curr.right != null) {
                q.offer(new Pair(curr.right, vertical + 1, level + 1));
            }
        }

        // Build the final result list
        for (var levels : map.values()) {
            ArrayList<Integer> curr = new ArrayList<>();

            for (var pq : levels.values()) {
                while (!pq.isEmpty()) {
                    curr.add(pq.poll());
                }
            }
            res.add(curr);
        }

        return res;
    }
}