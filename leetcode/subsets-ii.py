class Solution {

    HashSet<List<Integer>> set;

    void helper(int[] nums, int idx, List<Integer> curr, List<List<Integer>> ans) {

        if (idx == nums.length) {

            List<Integer> copy = new ArrayList<>(curr);

            if (!set.contains(copy)) {
                set.add(copy);
                ans.add(copy);
            }

            return;
        }

        // include current number
        curr.add(nums[idx]);
        helper(nums, idx + 1, curr, ans);
        curr.remove(curr.size() - 1);

        // exclude current number
        helper(nums, idx + 1, curr, ans);
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {

        Arrays.sort(nums); 

        set = new HashSet<>();
        List<List<Integer>> ans = new ArrayList<>();

        helper(nums, 0, new ArrayList<>(), ans);

        return ans;
    }
}