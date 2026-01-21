class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<>();

        while (!set.contains(n)) {
            set.add(n);

            n = helper(n);

            if (n == 1)
                return true;
        }

        return false;
    }

    int helper(int n) {
        int res = 0;

        while (n != 0) {
            int ln = n % 10;
            res += ln * ln;
            n /= 10;
        }

        return res;
    }

}