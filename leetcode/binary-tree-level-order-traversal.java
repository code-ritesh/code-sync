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

import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        // Final answer list to store each level's nodes separately
        List<List<Integer>> levelOrderList = new ArrayList<>();

        // Base case: if tree is empty
        if (root == null)
            return levelOrderList;

        // Queue to perform BFS (level order traversal)
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root); // Add root node to start traversal

        // Loop until queue becomes empty
        while (!queue.isEmpty()) {

            int levelSize = queue.size(); // Number of nodes in the current level
            List<Integer> currentLevel = new ArrayList<>();

            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {

                TreeNode currentNode = queue.poll(); // Remove front node
                currentLevel.add(currentNode.val);   // Add its value to the current level

                // Add left and right children to queue if they exist
                if (currentNode.left != null)
                    queue.offer(currentNode.left);

                if (currentNode.right != null)
                    queue.offer(currentNode.right);
            }

            // After processing one level, add it to the final list
            levelOrderList.add(currentLevel);
        }

        // Return the final level order traversal
        return levelOrderList;
    }
}