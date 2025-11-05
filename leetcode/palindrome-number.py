class Solution {
public:
    bool isPalindrome(int x) {

        if( x < 0 ) return false;

        int o  = x ;

        long  rev = 0 ;

        while(x != 0 ){
            int ln = x % 10;
            rev = (rev*10) + ln;
            x /= 10;
        }

        return o == rev;

        
    }
};