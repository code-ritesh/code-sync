class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;

        boolean help[] = new boolean[n + 1];

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x >= 1 && x <= n)
                help[x] = true;
        }

        for (int i = 1; i <= n; i++) {
            if (!help[i])
                return i;
        }

        return n + 1;
    }
}