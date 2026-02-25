class Solution {

    boolean isVowel(char ch) {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            return true;

        return false;
    }

    public int maxVowels(String s, int k) {
        int n = s.length();
        int c = 0;
        int max = 0;

        for(int i = 0 ; i < k ; i++){
            char ch = s.charAt(i);

            if( isVowel(ch) ) c++;
        }

        max = Math.max(c,max);

        for(int i = k ; i < n ; i++){
            char ch = s.charAt(i);

            if(isVowel(ch)) c++;
            if(isVowel(s.charAt(i-k))) c--;

            max = Math.max(c,max);

        } 

        return max;

    }
}