class Solution {
    public int longestCommonSubsequence(String a, String b) {
        int m = a.length();
        int n = b.length();

        int dp[][] = new int[m + 1][n + 1];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return helper(a, b, m, n, dp);
    }

    int helper(String a, String b, int m, int n, int[][] dp) {
        if (m == 0 || n == 0)
            return 0;

        if (dp[m][n] != -1)
            return dp[m][n];

        if (a.charAt(m - 1) == b.charAt(n - 1)) {
            return  dp[m][n] = 1 + helper(a, b, m - 1, n - 1 , dp);
        }

        else
            return dp[m][n] = Math.max(helper(a, b, m - 1, n,dp), helper(a, b, m, n - 1,dp));
    }
}