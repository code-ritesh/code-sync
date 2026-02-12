class Solution {
    public int maxSubArray(int[] nums) {
        int maxans = Integer.MIN_VALUE;

        int curr = 0;

        for(int i = 0 ; i < nums.length ; i++){
            curr = Math.max( nums[i] , curr + nums[i]); // to handle the negative case
            maxans = Math.max(curr,maxans);
        }

        return maxans;
    }
}