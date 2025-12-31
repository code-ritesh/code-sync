class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }

        if (sum % 2 != 0)
            return false;

        else {
            return subsetSum(nums, sum / 2);
        }

    }

    boolean subsetSum(int[] arr, int target) {

        int n = arr.length;

        boolean dp[][] = new boolean[arr.length + 1][target + 1];

        for (int i = 0; i <= n; i++) {
            dp[i][0] = true; // if target is 0
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= target; j++) {

                if (arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
                }

                else
                    dp[i][j] = dp[i - 1][j];
            }
        }

        return dp[n][target];
    }
}