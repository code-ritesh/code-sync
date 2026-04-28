class Solution {
    public int orangesRotting(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int cntfresh = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1)
                    cntfresh++;
                else if (grid[i][j] == 2) {
                    q.offer(new int[] { i, j, 0 });
                }
            }
        }

        int time = 0;
        int[] dr = { 0, 0, -1, 1 };
        int[] dc = { -1, 1, 0, 0 };

        while (!q.isEmpty()) {
            int[] polled = q.poll();
            int a = polled[0];
            int b = polled[1];
            int t = polled[2];

            time = Math.max(time, t);

            for (int i = 0; i < 4; i++) {
                int nr = a + dr[i];
                int nc = b + dc[i];

                if (nr < 0 || nc < 0 || nr >= n || nc >= m || grid[nr][nc] != 1)
                    continue;
                else {
                    q.offer(new int[] { nr, nc, t + 1 });
                    cntfresh--;
                    grid[nr][nc] = 0;
                }
            }
        }

        if (cntfresh == 0)
            return time;
        return -1;
    }
}