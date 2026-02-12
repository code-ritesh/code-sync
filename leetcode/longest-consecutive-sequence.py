class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        int curr = 1;
        int max = 0;
        int n = nums.length;

        if(n == 0 ) return 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                curr++;
            }

            else if (nums[i - 1] == nums[i])
                continue;

            else {
                curr = 1;
            }

            max = Math.max(curr, max);
        }

        return Math.max(curr, max);
    }
}