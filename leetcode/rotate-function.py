class Solution {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length ;
        int sum = 0;
        int old = 0;

        for(int i = 0 ; i < n ; i++){
            old += (i* nums[i]);
            sum += nums[i];
        }

        int res = old;

        for(int k = 0 ; k < n ; k++){
            int newf = old + sum - n* nums[n-1-k];
            res =  Math.max(newf,res);
            old = newf;
        }

        return res;
    }
}