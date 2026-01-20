class Solution {
    public int strStr(String haystack, String needle) {
        int ans = -1;

        int m = haystack.length();
        int n = needle.length();

        if(m < n ) return -1;

        for(int i =  0 ; i <= m-n ; i++){
            String x = haystack.substring(i,i+n);
            if(  x.equals(needle) ) return i;
        }

        return ans;
    }
}