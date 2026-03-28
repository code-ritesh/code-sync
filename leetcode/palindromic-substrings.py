class Solution {

    public int countSubstrings(String s) {
        int n = s.length();
        int count = 0;

        for (int i = 0; i < n; i++) {
            count += helper(s, i, i); // odd length
            count += helper(s, i, i + 1); //even length
        }

        return count;
    }

    int helper(String s, int i, int j) {

        int count = 0;

        while (j < s.length() && i >= 0 && s.charAt(i) == s.charAt(j)) {

            //System.out.println(s.substring(i, j + 1));
            count++;
            i--;
            j++;
        }

        return count;
    }
}