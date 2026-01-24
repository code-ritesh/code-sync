class Solution {
    public int superEggDrop(int egg, int floor) {
        int[][] dp = new int[floor + 1][egg + 1];
        int moves = 0;

        while (dp[moves][egg] < floor) {
            moves++;
            for (int e = 1; e <= egg; e++) {
                dp[moves][e] = dp[moves - 1][e - 1] +
                        dp[moves - 1][e] + 1;
            }
        }
        return moves;
    }
}