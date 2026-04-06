class Solution {
    public int[] applyOperations(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                nums[i] = 0;
                nums[i - 1] *= 2;
            }
        }

        int noz = 0;

        for (int x : nums) {
            if (x == 0)
                noz++;
        }

        int idx = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[idx] = nums[i];
                idx++;
            }
        }

        for (int i = idx; i < nums.length; i++)
            nums[idx++] = 0;

        return nums;
    }
}