class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int close = Integer.MAX_VALUE;
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];

                if (Math.abs(target - sum) < Math.abs(target - close)) {
                    close = sum;
                }

                if (sum == target)
                    return sum;
                else if (sum < target) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return close;
    }
}