/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> finalans = new ArrayList<>();

        if (root == null)
            return finalans;

        Queue<Node> q = new LinkedList<>();

        q.offer(root);

        while (!q.isEmpty()) {
            int n = q.size();

            List<Integer> res = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                Node curr = q.poll();

                res.add(curr.val);

                for (Node node : curr.children) {
                    q.offer(node);
                }
            }

            finalans.add(res);

        }

        return finalans;
    }
}