class Solution {
    public int reverse(int x) {
        if(x == 0 ) return x;

        int num = Math.abs(x);

        int  rev = 0;

        while(num != 0 ){
            int  ln = num % 10;
            if( rev > (Integer.MAX_VALUE - ln ) / 10)  return 0;
            rev = (rev*10) + ln;
            num /= 10;
        }

        if(x < 0 ) return -rev;
        return rev;
    }
}