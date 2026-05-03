class Solution {
    public boolean rotateString(String s, String goal) {
        int m = s.length();
        int n = goal.length();

        s = s+s;

        if(m == n && s.contains(goal)) return true;
        return false;
    }
}