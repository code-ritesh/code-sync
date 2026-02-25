class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;

        int suffix = 1;
        int prefix = 1;
        int ans = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            int x = nums[i];

            if (prefix == 0)
                prefix = 1;
            if (suffix == 0)
                suffix = 1;

            prefix *= nums[i];
            suffix *= nums[n - i - 1];

            ans = Math.max(ans, Math.max(suffix, prefix));
        }

        return ans;
    }
}