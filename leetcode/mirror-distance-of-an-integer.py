class Solution {
    public int mirrorDistance(int n) {
        int b = helper(n);

        return Math.abs(b-n);
    }

    int helper(int n){
        int rev= 0;

        while(n != 0){
            int ln = n % 10;
            rev = (rev*10) + ln;
            n /= 10;
        }

        return rev;
    }
}