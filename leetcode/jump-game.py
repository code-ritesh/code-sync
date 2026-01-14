class Solution {
    public boolean canJump(int[] nums) {
        int maxidx = 0;
        int n = nums.length;
        int i = 0;

        while(i <= maxidx ){
            maxidx = Math.max(maxidx , i + nums[i]);
            if( maxidx >= (n-1) ) return true;
            i++;
        }

        return false;
    }
}