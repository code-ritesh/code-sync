class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int s = 0;
        int e = 0;
        int ans = -1;

        for (int x : bloomDay) {
            s = Math.min(s, x);
            e = Math.max(e, x);
        }

        while (s <= e) {
            int mid = s + (e - s) / 2;

            if (possible(bloomDay, m, k, mid)) {
                ans = mid;
                e = mid - 1;
            }

            else
                s = mid + 1;
        }

        return ans;
    }

    boolean possible(int[] bloomDay, int m, int k, int mid) {
        int flower = 0;
        int nob = 0;

        for (int x : bloomDay) {
            if (x <= mid)
                flower++;

            else
                flower = 0;

            if (flower == k) {
                nob++;
                flower = 0;
            }

        }

        if (nob >= m)
            return true;

        return false;
    }
}