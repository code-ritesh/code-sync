class Solution {
    public int findKthPositive(int[] arr, int k) {
        Set<Integer> set = new HashSet<>();
        int ans = -1;

        for (int x : arr) {
            set.add(x);
        }

        for (int i = 1;; i++) {
            if (!set.contains(i)) {
                k--;
            }

            if (k == 0)
                return i;

        }

    }
}