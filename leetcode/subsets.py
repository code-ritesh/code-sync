class Solution {
    List<List<Integer>> result;

    public List<List<Integer>> subsets(int[] nums) {
        result = new ArrayList<>();   // ✅ initialize
        List<Integer> curr = new ArrayList<>();

        helper(nums, 0, curr);
        return result;
    }

    void helper(int[] nums, int idx, List<Integer> curr) {
        if (idx == nums.length) {
            result.add(new ArrayList<>(curr));
            return;
        }

        // include
        curr.add(nums[idx]);
        helper(nums, idx + 1, curr);

        // exclude
        curr.remove(curr.size() - 1);  // ✅ remove last added element
        helper(nums, idx + 1, curr);
    }
}