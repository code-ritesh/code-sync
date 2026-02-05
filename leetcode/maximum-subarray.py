class Solution {
    public int maxSubArray(int[] nums) {
        int maxans = 0;

        int curr = 0;

        for(int i = 0 ; i < nums.length ; i++){
            if(curr < 0 ){
                curr = 0 ;
            }

            curr += nums[i];

            maxans = Math.max(curr,maxans);
        }

        return maxans;
    }
}