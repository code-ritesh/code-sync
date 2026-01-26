class Solution {
    int[][] dp;

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        dp = new int[m][n];

        for (int[] r : dp)
            Arrays.fill(r, -1);

        return solve(obstacleGrid, 0, 0);
    }

    int solve(int[][] obstacleGrid, int i, int j) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        if (i < 0 || j < 0 || i >= m || j >= n || obstacleGrid[i][j] != 0)
            return 0;

        if (i == m - 1 && j == n - 1)
            return 1;

        if (dp[i][j] != -1)
            return dp[i][j];

        int temp = obstacleGrid[i][j];
        obstacleGrid[i][j] = 2;

        int right = solve(obstacleGrid, i + 1, j);
        int bottom = solve(obstacleGrid, i, j + 1);

        obstacleGrid[i][j] = temp;

        dp[i][j] = right + bottom;

        return dp[i][j];
    }
}