class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int cnt = 0;
        boolean[] visited = new boolean[n + 1];
        List<List<Integer>> adj = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j] == 1 && i != j) {
                    adj.get(i).add(j);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                cnt++;
                helper(adj, i, visited);
            }
        }

        return cnt;
    }

    void helper(List<List<Integer>> adj, int curr, boolean[] visited) {
        visited[curr] = true;

        for (int n : adj.get(curr)) {
            if (!visited[n]) {
                visited[n] = true;
                helper(adj, n, visited);
            }
        }

    }
}