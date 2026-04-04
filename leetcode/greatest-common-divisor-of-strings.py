class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        
        int a = str1.length();
        int b = str2.length();
        int len = 0;
        int x = Math.max(a,b);
        
        for(int i = x ; i >= 1 ; i--){
            if( a % i == 0 && b % i == 0 ){
                len = i;
                break;
            }
        }
        
        return str1.substring(0, len);
    }
}