class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        // same as partitions with given difference on gfg

        int n = nums.length;
        int range = 0;
        // target == diff

        for(int x : nums ) range += x;

        
        if(range < target || (target + range) % 2 == 1  ) return 0;

        int s1 = (range + target ) / 2;

        if (s1 < 0) return 0; 


        return helper(nums , s1);
    }


    int helper(int[] nums , int s1){
        int n = nums.length;

        int[][] dp = new int[n+1][s1+1];

        for(int i = 0; i <= n ; i++) dp[i][0] = 1;

        for(int i = 1 ; i <= n ; i++){
            for(int j = 0 ; j <= s1 ; j++){
                if(nums[i-1] <= j ){
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];
                }

                else dp[i][j] = dp[i-1][j];
            }
        }

        return dp[n][s1];
    }
}