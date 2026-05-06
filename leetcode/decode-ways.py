class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length() + 1];
        Arrays.fill(dp,-1);
        return solve(s, 0,dp);
    }

    int solve(String s, int idx , int[] dp) {
        int n = s.length();

        if (idx >= n)
            return 1;
        if (s.charAt(idx) == '0')
            return 0;

        if(dp[idx] != -1 ) return dp[idx];

        int count = solve(s, idx + 1,dp);

        if (idx + 2 <= n) {
            String str = s.substring(idx, idx + 2);
            if (Integer.parseInt(str) <= 26) {
                count += solve(s, idx + 2,dp);
            }
        }

        return dp[idx] = count;
    }
}