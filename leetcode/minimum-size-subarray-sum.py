class Solution {
    public int minSubArrayLen(int target, int[] nums) {

        int n = nums.length;
        int i = 0;
        int sum = 0;
        int minlen = Integer.MAX_VALUE;

        for (int j = 0; j < n; j++) {

            sum += nums[j];

            while (sum > target) {
                sum -= nums[i];
                i++;
            }

            if(sum == target ) minlen = Math.min(j-i+1,minlen);
        }

        return minlen == Integer.MAX_VALUE ? 0 : minlen;
    }
}