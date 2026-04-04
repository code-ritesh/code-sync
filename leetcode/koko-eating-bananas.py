class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int s = 1;
        int e = Integer.MIN_VALUE;

        for (int x : piles)
            e = Math.max(e, x);

        while (s < e) {
            int mid = s + (e - s) / 2;

            if (caneat(piles, mid, h))
                e = mid;
            else
                s = mid + 1;
        }

        return s;
    }

    boolean caneat(int[] piles, int mid, int h) {
        int ah = 0;

        for (int x : piles) {
            ah += x / mid;

            if (x % mid != 0)
                ah++;
        }

        if (ah <= h)
            return true;
        return false;
    }
}