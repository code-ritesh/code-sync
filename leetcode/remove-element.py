class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int idx = 0;

        for(int x : nums){
            if(x != val ){
                nums[idx++] = x;
            }
        }

        return idx;
    }
}