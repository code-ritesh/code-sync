class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();

        for (char x : s.toCharArray()) {
            if (x == '(')  st.add(')');
            else if (x == '{') st.add('}');
            else if (x == '[') st.add(']');

            else if (st.isEmpty() || st.peek() != x)
                return false;

            else st.pop();
        }

        return st.isEmpty();
    }
}