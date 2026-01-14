class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int maxidx = 0;
        int count = 0;
        int end = 0 ;
        

        for(int i = 0  ; i < n - 1 ; i++){
            maxidx = Math.max(maxidx , i + nums[i]);

            if(i == end ){
                count++;
                end = maxidx;
            }
        }

        return count;
    }
}